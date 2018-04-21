#!/bin/py
import os
import sys
import subprocess
import json

try:
    token_code = raw_input("Please enter a token code: ")
    try: mfa_arn = os.environ['MFA_ARN']
    except KeyError:
        print "\nYour default MFA Device ARN is not set. To set a default, use the environmental variable $MFA_ARN."
        mfa_arn = raw_input("For now, please enter an mfa device arn: ")
    cmd = "aws sts get-session-token --serial-number "+mfa_arn+" --token-code "+token_code+" --duration-seconds 64800"
    result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    out, err = result.communicate()
    if result.returncode !=0: sys.exit("Please read the above message and try again.")

    out=json.loads(out)
    print

    cmd = "export AWS_SECRET_ACCESS_KEY="+out["Credentials"]["SecretAccessKey"]+"&&export AWS_SESSION_TOKEN="+out["Credentials"]["SessionToken"]+"&&export AWS_ACCESS_KEY_ID="+out["Credentials"]["AccessKeyId"]
    success = "&& echo 'AWS Session token successfully set!'"
    try:
        filename = os.path.expanduser('~')+'/.AWS_CREDENTIAL_EXPORT'
        if not os.path.exists(filename): open(filename,'a').close()
        with open(filename,'r+') as fp:
            fp.truncate()
            fp.write(cmd+success)
            fp.close()
    except IOError:
        print "Could not completely set your AWS Token. You must take the last step. Please run the below command:\n"
        print cmd
except KeyboardInterrupt:
    sys.exit("\nOkay... have a nice day!")