# accessanalyzerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# accessanalyzer

## Description

Identity and Access Management Access Analyzer helps you to set, verify, and refine your IAM policies by providing a suite of capabilities. Its features include findings for external and unused access, basic and custom policy checks for validating policies, and policy generation to generate fine-grained policies. To start using IAM Access Analyzer to identify external or unused access, you first need to create an analyzer.

**External access analyzers** help identify potential risks of accessing resources by enabling you to identify any resource policies that grant access to an external principal. It does this by using logic-based reasoning to analyze resource-based policies in your Amazon Web Services environment. An external principal can be another Amazon Web Services account, a root user, an IAM user or role, a federated user, an Amazon Web Services service, or an anonymous user. You can also use IAM Access Analyzer to preview public and cross-account access to your resources before deploying permissions changes.

**Unused access analyzers** help identify potential identity access risks by enabling you to identify unused IAM roles, unused access keys, unused console passwords, and IAM principals with unused service and action-level permissions.

Beyond findings, IAM Access Analyzer provides basic and custom policy checks to validate IAM policies before deploying permissions changes. You can use policy generation to refine permissions by attaching a policy generated using access activity logged in CloudTrail logs.

This guide describes the IAM Access Analyzer operations that you can call programmatically. For general information about IAM Access Analyzer, see [Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) in the **IAM User Guide** .

## Available Commands

- [apply-archive-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/apply-archive-rule.html)
- [cancel-policy-generation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/cancel-policy-generation.html)
- [check-access-not-granted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-access-not-granted.html)
- [check-no-new-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-no-new-access.html)
- [check-no-public-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-no-public-access.html)
- [create-access-preview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-access-preview.html)
- [create-analyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-analyzer.html)
- [create-archive-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-archive-rule.html)
- [delete-analyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-analyzer.html)
- [delete-archive-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-archive-rule.html)
- [generate-finding-recommendation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/generate-finding-recommendation.html)
- [get-access-preview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-access-preview.html)
- [get-analyzed-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzed-resource.html)
- [get-analyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzer.html)
- [get-archive-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-archive-rule.html)
- [get-finding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding.html)
- [get-finding-recommendation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding-recommendation.html)
- [get-finding-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding-v2.html)
- [get-findings-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-findings-statistics.html)
- [get-generated-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-generated-policy.html)
- [list-access-preview-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-access-preview-findings.html)
- [list-access-previews](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-access-previews.html)
- [list-analyzed-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzed-resources.html)
- [list-analyzers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzers.html)
- [list-archive-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-archive-rules.html)
- [list-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings.html)
- [list-findings-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings-v2.html)
- [list-policy-generations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-policy-generations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-tags-for-resource.html)
- [start-policy-generation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/start-policy-generation.html)
- [start-resource-scan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/start-resource-scan.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/untag-resource.html)
- [update-analyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-analyzer.html)
- [update-archive-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-archive-rule.html)
- [update-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-findings.html)
- [validate-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/validate-policy.html)