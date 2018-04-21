# General
### Purpose
This *python* script automates aws cli mfa session token and key fetching, and places a command in a file to be sourced by your shell.

### Use
The python script, alone, simply updates (or creates) a file at `~/.AWS_CREDENTIAL_EXPORT` to contain a shell export command needed to set the relevant environmental variables that amazon looks for. If you wanted, you could individually run the script and then run the command `source ~/.AWS_CREDENTIAL_EXPORT`, but I recommend using aliases. Please see the configuration instructions below:

# Config
### Requirements
This script requires the `aws cli` and `python`. Setup instructions rely on a common shell (e.g. `bash` or `zsh`).

### General Setup & Alias Configuration
It is recommended to configure a shell alias to handle this. See as follows: 
1. Using your shell, move into the directory containing this file.
1. Move `.AWS_MFA_TOKEN.py` to your home (`~`) directory. To do this, try the following command:
```mv .AWS_MFA_TOKEN.py ~/.AWS_MFA_TOKEN.py```
1. Make `.AWS_MFA_TOKEN` user-executable. To do this, try running the following command:
```chmod +ux ~/.AWS_MFA_TOKEN.py```
1. Add the relevant aliases (see below) to your shell's profile (and re-source the profile).
    * `alias awstoken='python ~/.AWS_MFA_TOKEN.py && source ~/.AWS_CREDENTIAL_EXPORT'`
    * `alias awstokencache='source ~/.AWS_CREDENTIAL_EXPORT && echo "Using cached AWS Token"'`
    * To do this for *bash*, run the following command:`echo -e "alias awstoken='python ~/.AWS_MFA_TOKEN.py && source ~/.AWS_CREDENTIAL_EXPORT'\nalias awstokencache='source ~/.AWS_CREDENTIAL_EXPORT && echo Using cached AWS Token'" >> ~/.bash_profile && source ~/.bash_profile`

You're now set up! Just type `awstoken` into any window to set up a new MFA session for the current shell session. To configure a shell to use an already-active session, type `awstokencache`.

### MFA ARN Configuration
This script relies on a code from your MFA device. You can use the environment variable `MFA_ARN` to remember a default arn.

To do this, get your mfa device's arn from AWS IAM and add an export statement to your shell's profile:
    * `export MFA_ARN=your-MFA-Device-ARN`
    *To do this for *bash*, run the following command:```echo "export MFA_ARN=your-MFA-Device-ARN" >> ~/.bash_profile && source ~/.bash_profile```
