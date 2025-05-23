# ecrÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# ecr

## Description

Amazon Elastic Container Registry (Amazon ECR) is a managed container image registry service. Customers can use the familiar Docker CLI, or their preferred client, to push, pull, and manage images. Amazon ECR provides a secure, scalable, and reliable registry for your Docker or Open Container Initiative (OCI) images. Amazon ECR supports private repositories with resource-based permissions using IAM so that specific users or Amazon EC2 instances can access repositories and images.

Amazon ECR has service endpoints in each supported Region. For more information, see [Amazon ECR endpoints](https://docs.aws.amazon.com/general/latest/gr/ecr.html) in the *Amazon Web Services General Reference* .

## Available Commands

- [batch-check-layer-availability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-check-layer-availability.html)
- [batch-delete-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-delete-image.html)
- [batch-get-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-get-image.html)
- [batch-get-repository-scanning-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-get-repository-scanning-configuration.html)
- [complete-layer-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/complete-layer-upload.html)
- [create-pull-through-cache-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-pull-through-cache-rule.html)
- [create-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html)
- [create-repository-creation-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository-creation-template.html)
- [delete-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-lifecycle-policy.html)
- [delete-pull-through-cache-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-pull-through-cache-rule.html)
- [delete-registry-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-registry-policy.html)
- [delete-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository.html)
- [delete-repository-creation-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository-creation-template.html)
- [delete-repository-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository-policy.html)
- [describe-image-replication-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-image-replication-status.html)
- [describe-image-scan-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-image-scan-findings.html)
- [describe-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-images.html)
- [describe-pull-through-cache-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-pull-through-cache-rules.html)
- [describe-registry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-registry.html)
- [describe-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repositories.html)
- [describe-repository-creation-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repository-creation-templates.html)
- [get-account-setting](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-account-setting.html)
- [get-authorization-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-authorization-token.html)
- [get-download-url-for-layer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-download-url-for-layer.html)
- [get-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-lifecycle-policy.html)
- [get-lifecycle-policy-preview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-lifecycle-policy-preview.html)
- [get-login-password](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login-password.html)
- [get-registry-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-registry-policy.html)
- [get-registry-scanning-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-registry-scanning-configuration.html)
- [get-repository-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-repository-policy.html)
- [initiate-layer-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/initiate-layer-upload.html)
- [list-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-images.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-tags-for-resource.html)
- [put-account-setting](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-account-setting.html)
- [put-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image.html)
- [put-image-scanning-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image-scanning-configuration.html)
- [put-image-tag-mutability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image-tag-mutability.html)
- [put-lifecycle-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-lifecycle-policy.html)
- [put-registry-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-registry-policy.html)
- [put-registry-scanning-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-registry-scanning-configuration.html)
- [put-replication-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-replication-configuration.html)
- [set-repository-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/set-repository-policy.html)
- [start-image-scan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-image-scan.html)
- [start-lifecycle-policy-preview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-lifecycle-policy-preview.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/untag-resource.html)
- [update-pull-through-cache-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/update-pull-through-cache-rule.html)
- [update-repository-creation-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/update-repository-creation-template.html)
- [upload-layer-part](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/upload-layer-part.html)
- [validate-pull-through-cache-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/validate-pull-through-cache-rule.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/wait/index.html)