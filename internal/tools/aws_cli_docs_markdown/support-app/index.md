# support-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# support-app

## Description

You can use the Amazon Web Services Support App in Slack API to manage your support cases in Slack for your Amazon Web Services account. After you configure your Slack workspace and channel with the Amazon Web Services Support App, you can perform the following tasks directly in your Slack channel:

- Create, search, update, and resolve your support cases
- Request service quota increases for your account
- Invite Amazon Web Services Support agents to your channel so that you can chat directly about your support cases

For more information about how to perform these actions in Slack, see the following documentation in the *Amazon Web Services Support User Guide* :

- [Amazon Web Services Support App in Slack](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html)
- [Joining a live chat session with Amazon Web Services Support](https://docs.aws.amazon.com/awssupport/latest/user/joining-a-live-chat-session.html)
- [Requesting service quota increases](https://docs.aws.amazon.com/awssupport/latest/user/service-quota-increase.html)
- [Amazon Web Services Support App commands in Slack](https://docs.aws.amazon.com/awssupport/latest/user/support-app-commands.html)

You can also use the Amazon Web Services Management Console instead of the Amazon Web Services Support App API to manage your Slack configurations. For more information, see [Authorize a Slack workspace to enable the Amazon Web Services Support App](https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html) .

### Note

- You must have a Business or Enterprise Support plan to use the Amazon Web Services Support App API.
- For more information about the Amazon Web Services Support App endpoints, see the [Amazon Web Services Support App in Slack endpoints](https://docs.aws.amazon.com/general/latest/gr/awssupport.html#awssupport_app_region) in the *Amazon Web Services General Reference* .

## Available Commands

- [create-slack-channel-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/create-slack-channel-configuration.html)
- [delete-account-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/delete-account-alias.html)
- [delete-slack-channel-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/delete-slack-channel-configuration.html)
- [delete-slack-workspace-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/delete-slack-workspace-configuration.html)
- [get-account-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/get-account-alias.html)
- [list-slack-channel-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/list-slack-channel-configurations.html)
- [list-slack-workspace-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/list-slack-workspace-configurations.html)
- [put-account-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/put-account-alias.html)
- [register-slack-workspace-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/register-slack-workspace-for-organization.html)
- [update-slack-channel-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/update-slack-channel-configuration.html)