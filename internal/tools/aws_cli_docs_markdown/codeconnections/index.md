# codeconnectionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codeconnections

## Description

This Amazon Web Services CodeConnections API Reference provides descriptions and usage examples of the operations and data types for the Amazon Web Services CodeConnections API. You can use the connections API to work with connections and installations.

*Connections* are configurations that you use to connect Amazon Web Services resources to external code repositories. Each connection is a resource that can be given to services such as CodePipeline to connect to a third-party repository such as Bitbucket. For example, you can add the connection in CodePipeline so that it triggers your pipeline when a code change is made to your third-party code repository. Each connection is named and associated with a unique ARN that is used to reference the connection.

When you create a connection, the console initiates a third-party connection handshake. *Installations* are the apps that are used to conduct this handshake. For example, the installation for the Bitbucket provider type is the Bitbucket app. When you create a connection, you can choose an existing installation or create one.

When you want to create a connection to an installed provider type such as GitHub Enterprise Server, you create a *host* for your connections.

You can work with connections by calling:

- CreateConnection , which creates a uniquely named connection that can be referenced by services such as CodePipeline.
- DeleteConnection , which deletes the specified connection.
- GetConnection , which returns information about the connection, including the connection status.
- ListConnections , which lists the connections associated with your account.

You can work with hosts by calling:

- CreateHost , which creates a host that represents the infrastructure where your provider is installed.
- DeleteHost , which deletes the specified host.
- GetHost , which returns information about the host, including the setup status.
- ListHosts , which lists the hosts associated with your account.

You can work with tags in Amazon Web Services CodeConnections by calling the following:

- ListTagsForResource , which gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in Amazon Web Services CodeConnections.
- TagResource , which adds or updates tags for a resource in Amazon Web Services CodeConnections.
- UntagResource , which removes tags for a resource in Amazon Web Services CodeConnections.

For information about how to use Amazon Web Services CodeConnections, see the [Developer Tools User Guide](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html) .

## Available Commands

- [create-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/create-connection.html)
- [create-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/create-host.html)
- [create-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/create-repository-link.html)
- [create-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/create-sync-configuration.html)
- [delete-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/delete-connection.html)
- [delete-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/delete-host.html)
- [delete-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/delete-repository-link.html)
- [delete-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/delete-sync-configuration.html)
- [get-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-connection.html)
- [get-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-host.html)
- [get-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-repository-link.html)
- [get-repository-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-repository-sync-status.html)
- [get-resource-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-resource-sync-status.html)
- [get-sync-blocker-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-sync-blocker-summary.html)
- [get-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-sync-configuration.html)
- [list-connections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/list-connections.html)
- [list-hosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/list-hosts.html)
- [list-repository-links](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/list-repository-links.html)
- [list-repository-sync-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/list-repository-sync-definitions.html)
- [list-sync-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/list-sync-configurations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/untag-resource.html)
- [update-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/update-host.html)
- [update-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/update-repository-link.html)
- [update-sync-blocker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/update-sync-blocker.html)
- [update-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/update-sync-configuration.html)