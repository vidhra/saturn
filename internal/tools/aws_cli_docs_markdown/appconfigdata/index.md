# appconfigdataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# appconfigdata

## Description

AppConfig Data provides the data plane APIs your application uses to retrieve configuration data. Hereâs how it works:

Your application retrieves configuration data by first establishing a configuration session using the AppConfig Data  StartConfigurationSession API action. Your sessionâs client then makes periodic calls to  GetLatestConfiguration to check for and retrieve the latest data available.

When calling `StartConfigurationSession` , your code sends the following information:

- Identifiers (ID or name) of an AppConfig application, environment, and configuration profile that the session tracks.
- (Optional) The minimum amount of time the sessionâs client must wait between calls to `GetLatestConfiguration` .

In response, AppConfig provides an `InitialConfigurationToken` to be given to the sessionâs client and used the first time it calls `GetLatestConfiguration` for that session.

### Warning

This token should only be used once in your first call to `GetLatestConfiguration` . You *must* use the new token in the `GetLatestConfiguration` response (`NextPollConfigurationToken` ) in each subsequent call to `GetLatestConfiguration` .

When calling `GetLatestConfiguration` , your client code sends the most recent `ConfigurationToken` value it has and receives in response:

- `NextPollConfigurationToken` : the `ConfigurationToken` value to use on the next call to `GetLatestConfiguration` .
- `NextPollIntervalInSeconds` : the duration the client should wait before making its next call to `GetLatestConfiguration` . This duration may vary over the course of the session, so it should be used instead of the value sent on the `StartConfigurationSession` call.
- The configuration: the latest data intended for the session. This may be empty if the client already has the latest version of the configuration.

### Warning

The `InitialConfigurationToken` and `NextPollConfigurationToken` should only be used once. To support long poll use cases, the tokens are valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException` .

For more information and to view example CLI commands that show how to retrieve a configuration using the AppConfig Data `StartConfigurationSession` and `GetLatestConfiguration` API actions, see [Retrieving the configuration](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration) in the *AppConfig User Guide* .

## Available Commands

- [get-latest-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/get-latest-configuration.html)
- [start-configuration-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/start-configuration-session.html)