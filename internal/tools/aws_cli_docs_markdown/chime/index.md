# chimeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# chime

## Description

### Warning

**Most of these APIs are no longer supported and will not be updated.** We recommend using the latest versions in the [Amazon Chime SDK API reference](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/welcome.html) , in the Amazon Chime SDK.

Using the latest versions requires migrating to dedicated namespaces. For more information, refer to [Migrating from the Amazon Chime namespace](https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html) in the *Amazon Chime SDK Developer Guide* .

The Amazon Chime application programming interface (API) is designed so administrators can perform key tasks, such as creating and managing Amazon Chime accounts, users, and Voice Connectors. This guide provides detailed information about the Amazon Chime API, including operations, types, inputs and outputs, and error codes.

You can use an AWS SDK, the AWS Command Line Interface (AWS CLI), or the REST API to make API calls for Amazon Chime. We recommend using an AWS SDK or the AWS CLI. The page for each API action contains a *See Also* section that includes links to information about using the action with a language-specific AWS SDK or the AWS CLI.

Using an AWS SDK

You donât need to write code to calculate a signature for request authentication. The SDK clients authenticate your requests by using access keys that you provide. For more information about AWS SDKs, see the [AWS Developer Center](http://aws.amazon.com/developer/) .

Using the AWS CLI

Use your access keys with the AWS CLI to make API calls. For information about setting up the AWS CLI, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS Command Line Interface User Guide* . For a list of available Amazon Chime commands, see the [Amazon Chime commands](https://docs.aws.amazon.com/cli/latest/reference/chime/index.html) in the *AWS CLI Command Reference* .

Using REST APIs

If you use REST to make API calls, you must authenticate your request by providing a signature. Amazon Chime supports Signature Version 4. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon Web Services General Reference* .

When making REST API calls, use the service name `chime` and REST endpoint `https://service.chime.aws.amazon.com` .

Administrative permissions are controlled using AWS Identity and Access Management (IAM). For more information, see [Identity and Access Management for Amazon Chime](https://docs.aws.amazon.com/chime/latest/ag/security-iam.html) in the *Amazon Chime Administration Guide* .

## Available Commands

- [associate-phone-number-with-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/associate-phone-number-with-user.html)
- [associate-signin-delegate-groups-with-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/associate-signin-delegate-groups-with-account.html)
- [batch-create-room-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-create-room-membership.html)
- [batch-delete-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-delete-phone-number.html)
- [batch-suspend-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-suspend-user.html)
- [batch-unsuspend-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-unsuspend-user.html)
- [batch-update-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-update-phone-number.html)
- [batch-update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/batch-update-user.html)
- [create-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-account.html)
- [create-bot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-bot.html)
- [create-meeting-dial-out](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-meeting-dial-out.html)
- [create-phone-number-order](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-phone-number-order.html)
- [create-room](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room.html)
- [create-room-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room-membership.html)
- [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-user.html)
- [delete-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-account.html)
- [delete-events-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-events-configuration.html)
- [delete-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-phone-number.html)
- [delete-room](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room.html)
- [delete-room-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-room-membership.html)
- [disassociate-phone-number-from-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/disassociate-phone-number-from-user.html)
- [disassociate-signin-delegate-groups-from-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/disassociate-signin-delegate-groups-from-account.html)
- [get-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account.html)
- [get-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-account-settings.html)
- [get-bot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-bot.html)
- [get-events-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-events-configuration.html)
- [get-global-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-global-settings.html)
- [get-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number.html)
- [get-phone-number-order](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number-order.html)
- [get-phone-number-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number-settings.html)
- [get-retention-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-retention-settings.html)
- [get-room](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-room.html)
- [get-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user.html)
- [get-user-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-user-settings.html)
- [invite-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/invite-users.html)
- [list-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-accounts.html)
- [list-bots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-bots.html)
- [list-phone-number-orders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-number-orders.html)
- [list-phone-numbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-numbers.html)
- [list-room-memberships](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-room-memberships.html)
- [list-rooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-rooms.html)
- [list-supported-phone-number-countries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-supported-phone-number-countries.html)
- [list-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-users.html)
- [logout-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/logout-user.html)
- [put-events-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-events-configuration.html)
- [put-retention-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-retention-settings.html)
- [redact-conversation-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/redact-conversation-message.html)
- [redact-room-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/redact-room-message.html)
- [regenerate-security-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/regenerate-security-token.html)
- [reset-personal-pin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/reset-personal-pin.html)
- [restore-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/restore-phone-number.html)
- [search-available-phone-numbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/search-available-phone-numbers.html)
- [update-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-account.html)
- [update-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-account-settings.html)
- [update-bot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-bot.html)
- [update-global-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-global-settings.html)
- [update-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html)
- [update-phone-number-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number-settings.html)
- [update-room](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room.html)
- [update-room-membership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room-membership.html)
- [update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html)
- [update-user-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user-settings.html)