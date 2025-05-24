# credential-helperÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/credential-helper/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/credential-helper/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# credential-helper

## Description

Provide a SigV4 compatible user name and password for git smart HTTP  These commands are consumed by git and should not used directly. Erase and Store are no-ops. Get is operation to generate credentials to authenticate AWS CodeCommit. Run âaws codecommit credential-helper helpâ for details

## Synopsis

```
aws codecommit credential-helper
```

## Options

*None*

## Available Commands

- [get](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/credential-helper/get.html)

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To set up the credential helper included in the AWS CLI with AWS CodeCommit**

The `credential-helper` utility is not designed to be called directly from the AWS CLI. Instead it is intended to be used as a parameter with the `git config` command to set up your local computer. It enables Git to use HTTPS and a cryptographically signed version of your IAM user credentials or Amazon EC2 instance role whenever Git needs to authenticate with AWS to interact with CodeCommit repositories.

```
git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
```

Output:

```
[credential]
    helper = !aws codecommit credential-helper $@
    UseHttpPath = true
```

For more information, see [Setting up for AWS CodeCommit Using Other Methods](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html?shortFooter=true#setting-up-other) in the *AWS CodeCommit User Guide*. Review the content carefully, and then follow the procedures in one of the following topics: [For HTTPS Connections on Linux, macOS, or Unix](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html) or [For HTTPS Connections on Windows](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-windows.html) in the *AWS CodeCommit User Guide*.