# protonÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# proton

## Description

This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the [actions](https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html) and [data types](https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html) for the Proton service.

The documentation for each action shows the Query API request parameters and the XML response.

Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the [Amazon Web Services Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) .

The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.

Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.

When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service *create* , *list* , *update* and *delete* API operations and the service instance *list* and *update* API operations.

To learn more about Proton, see the [Proton User Guide](https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html) .

**Ensuring Idempotency**

When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before theyâre complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.

*Idempotency* ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.

The following lists of APIs are grouped according to methods that ensure idempotency.

**Idempotent create APIs with a client token**

The API actions in this list support idempotency with the use of a *client token* . The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you *donât* reuse the same client token for other API requests. If you donât provide a client token for these APIs, a default client token is automatically provided by SDKs.

Given a request action that has succeeded:

If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.

If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a `ValidationException` with an `IdempotentParameterMismatch` error.

Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.

If the original resource is deleted and you retry the request, a new resource is created.

Idempotent create APIs with a client token:

- CreateEnvironmentTemplateVersion
- CreateServiceTemplateVersion
- CreateEnvironmentAccountConnection

**Idempotent create APIs**

Given a request action that has succeeded:

If you retry the request with an API from this group, and the original resource *hasnât* been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.

If the original resource has been modified, the retry throws a `ConflictException` .

If you retry with different input parameters, the retry throws a `ValidationException` with an `IdempotentParameterMismatch` error.

Idempotent create APIs:

- CreateEnvironmentTemplate
- CreateServiceTemplate
- CreateEnvironment
- CreateService

**Idempotent delete APIs**

Given a request action that has succeeded:

When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.

If you retry and the resource doesnât exist, the response is empty.

In both cases, the retry succeeds.

Idempotent delete APIs:

- DeleteEnvironmentTemplate
- DeleteEnvironmentTemplateVersion
- DeleteServiceTemplate
- DeleteServiceTemplateVersion
- DeleteEnvironmentAccountConnection

**Asynchronous idempotent delete APIs**

Given a request action that has succeeded:

If you retry the request with an API from this group, if the original request delete operation status is `DELETE_IN_PROGRESS` , the retry returns the resource detail data in the response without performing any further actions.

If the original request delete operation is complete, a retry returns an empty response.

Asynchronous idempotent delete APIs:

- DeleteEnvironment
- DeleteService

## Available Commands

- [accept-environment-account-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/accept-environment-account-connection.html)
- [cancel-component-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/cancel-component-deployment.html)
- [cancel-environment-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/cancel-environment-deployment.html)
- [cancel-service-instance-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/cancel-service-instance-deployment.html)
- [cancel-service-pipeline-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/cancel-service-pipeline-deployment.html)
- [create-component](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-component.html)
- [create-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-environment.html)
- [create-environment-account-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-environment-account-connection.html)
- [create-environment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-environment-template.html)
- [create-environment-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-environment-template-version.html)
- [create-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-repository.html)
- [create-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service.html)
- [create-service-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-instance.html)
- [create-service-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-sync-config.html)
- [create-service-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-template.html)
- [create-service-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-service-template-version.html)
- [create-template-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-template-sync-config.html)
- [delete-component](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-component.html)
- [delete-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-deployment.html)
- [delete-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-environment.html)
- [delete-environment-account-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-environment-account-connection.html)
- [delete-environment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-environment-template.html)
- [delete-environment-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-environment-template-version.html)
- [delete-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-repository.html)
- [delete-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service.html)
- [delete-service-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service-sync-config.html)
- [delete-service-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service-template.html)
- [delete-service-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-service-template-version.html)
- [delete-template-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/delete-template-sync-config.html)
- [get-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-account-settings.html)
- [get-component](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-component.html)
- [get-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-deployment.html)
- [get-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-environment.html)
- [get-environment-account-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-environment-account-connection.html)
- [get-environment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-environment-template.html)
- [get-environment-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-environment-template-version.html)
- [get-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-repository.html)
- [get-repository-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-repository-sync-status.html)
- [get-resources-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-resources-summary.html)
- [get-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service.html)
- [get-service-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-instance.html)
- [get-service-instance-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-instance-sync-status.html)
- [get-service-sync-blocker-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-sync-blocker-summary.html)
- [get-service-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-sync-config.html)
- [get-service-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-template.html)
- [get-service-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-service-template-version.html)
- [get-template-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-template-sync-config.html)
- [get-template-sync-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-template-sync-status.html)
- [list-component-outputs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-component-outputs.html)
- [list-component-provisioned-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-component-provisioned-resources.html)
- [list-components](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-components.html)
- [list-deployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-deployments.html)
- [list-environment-account-connections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-environment-account-connections.html)
- [list-environment-outputs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-environment-outputs.html)
- [list-environment-provisioned-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-environment-provisioned-resources.html)
- [list-environment-template-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-environment-template-versions.html)
- [list-environment-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-environment-templates.html)
- [list-environments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-environments.html)
- [list-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-repositories.html)
- [list-repository-sync-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-repository-sync-definitions.html)
- [list-service-instance-outputs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-instance-outputs.html)
- [list-service-instance-provisioned-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-instance-provisioned-resources.html)
- [list-service-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-instances.html)
- [list-service-pipeline-outputs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-pipeline-outputs.html)
- [list-service-pipeline-provisioned-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-pipeline-provisioned-resources.html)
- [list-service-template-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-template-versions.html)
- [list-service-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-service-templates.html)
- [list-services](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-services.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/list-tags-for-resource.html)
- [notify-resource-deployment-status-change](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/notify-resource-deployment-status-change.html)
- [reject-environment-account-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/reject-environment-account-connection.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/untag-resource.html)
- [update-account-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-account-settings.html)
- [update-component](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-component.html)
- [update-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-environment.html)
- [update-environment-account-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-environment-account-connection.html)
- [update-environment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-environment-template.html)
- [update-environment-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-environment-template-version.html)
- [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service.html)
- [update-service-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-instance.html)
- [update-service-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-pipeline.html)
- [update-service-sync-blocker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-sync-blocker.html)
- [update-service-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-sync-config.html)
- [update-service-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-template.html)
- [update-service-template-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-template-version.html)
- [update-template-sync-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-template-sync-config.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/wait/index.html)