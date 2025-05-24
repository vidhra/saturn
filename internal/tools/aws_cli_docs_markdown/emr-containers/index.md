# emr-containersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# emr-containers

## Description

Amazon EMR on EKS provides a deployment option for Amazon EMR that allows you to run open-source big data frameworks on Amazon Elastic Kubernetes Service (Amazon EKS). With this deployment option, you can focus on running analytics workloads while Amazon EMR on EKS builds, configures, and manages containers for open-source applications. For more information about Amazon EMR on EKS concepts and tasks, see [What is Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html) .

*Amazon EMR containers* is the API name for Amazon EMR on EKS. The `emr-containers` prefix is used in the following scenarios:

- It is the prefix in the CLI commands for Amazon EMR on EKS. For example, `aws emr-containers start-job-run` .
- It is the prefix before IAM policy actions for Amazon EMR on EKS. For example, `"Action": [ "emr-containers:StartJobRun"]` . For more information, see [Policy actions for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-actions) .
- It is the prefix used in Amazon EMR on EKS service endpoints. For example, `emr-containers.us-east-2.amazonaws.com` . For more information, see [Amazon EMR on EKSService Endpoints](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/service-quotas.html#service-endpoints) .

## Available Commands

- [cancel-job-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/cancel-job-run.html)
- [create-job-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-job-template.html)
- [create-managed-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-managed-endpoint.html)
- [create-role-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-role-associations.html)
- [create-security-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-security-configuration.html)
- [create-virtual-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/create-virtual-cluster.html)
- [delete-job-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/delete-job-template.html)
- [delete-managed-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/delete-managed-endpoint.html)
- [delete-role-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/delete-role-associations.html)
- [delete-virtual-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/delete-virtual-cluster.html)
- [describe-job-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-job-run.html)
- [describe-job-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-job-template.html)
- [describe-managed-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-managed-endpoint.html)
- [describe-security-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-security-configuration.html)
- [describe-virtual-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-virtual-cluster.html)
- [get-managed-endpoint-session-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/get-managed-endpoint-session-credentials.html)
- [list-job-runs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-job-runs.html)
- [list-job-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-job-templates.html)
- [list-managed-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-managed-endpoints.html)
- [list-security-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-security-configurations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-tags-for-resource.html)
- [list-virtual-clusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-virtual-clusters.html)
- [start-job-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/start-job-run.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/untag-resource.html)
- [update-role-trust-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/update-role-trust-policy.html)