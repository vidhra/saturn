# codestar-connectionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codestar-connections

## Description

This Amazon Web Services CodeStar Connections API Reference provides descriptions and usage examples of the operations and data types for the Amazon Web Services CodeStar Connections API. You can use the connections API to work with connections and installations.

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

You can work with tags in Amazon Web Services CodeStar Connections by calling the following:

- ListTagsForResource , which gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in Amazon Web Services CodeStar Connections.
- TagResource , which adds or updates tags for a resource in Amazon Web Services CodeStar Connections.
- UntagResource , which removes tags for a resource in Amazon Web Services CodeStar Connections.

For information about how to use Amazon Web Services CodeStar Connections, see the [Developer Tools User Guide](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html) .

## Available Commands

- [create-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-connection.html)
- [create-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-host.html)
- [create-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-repository-link.html)
- [create-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-sync-configuration.html)
- [delete-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-connection.html)
- [delete-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-host.html)
- [delete-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-repository-link.html)
- [delete-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-sync-configuration.html)
- [get-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-connection.html)
- [get-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-host.html)
- [get-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-repository-link.html)
- [get-repository-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-repository-sync-status.html)
- [get-resource-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-resource-sync-status.html)
- [get-sync-blocker-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-sync-blocker-summary.html)
- [get-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-sync-configuration.html)
- [list-connections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-connections.html)
- [list-hosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-hosts.html)
- [list-repository-links](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-repository-links.html)
- [list-repository-sync-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-repository-sync-definitions.html)
- [list-sync-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-sync-configurations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/untag-resource.html)
- [update-host](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/update-host.html)
- [update-repository-link](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/update-repository-link.html)
- [update-sync-blocker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/update-sync-blocker.html)
- [update-sync-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/update-sync-configuration.html)