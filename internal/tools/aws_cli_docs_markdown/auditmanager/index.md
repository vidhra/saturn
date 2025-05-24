# auditmanagerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# auditmanager

## Description

Welcome to the Audit Manager API reference. This guide is for developers who need detailed information about the Audit Manager API operations, data types, and errors.

Audit Manager is a service that provides automated evidence collection so that you can continually audit your Amazon Web Services usage. You can use it to assess the effectiveness of your controls, manage risk, and simplify compliance.

Audit Manager provides prebuilt frameworks that structure and automate assessments for a given compliance standard. Frameworks include a prebuilt collection of controls with descriptions and testing procedures. These controls are grouped according to the requirements of the specified compliance standard or regulation. You can also customize frameworks and controls to support internal audits with specific requirements.

Use the following links to get started with the Audit Manager API:

- [Actions](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Operations.html) : An alphabetical list of all Audit Manager API operations.
- [Data types](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Types.html) : An alphabetical list of all Audit Manager data types.
- [Common parameters](https://docs.aws.amazon.com/audit-manager/latest/APIReference/CommonParameters.html) : Parameters that all operations can use.
- [Common errors](https://docs.aws.amazon.com/audit-manager/latest/APIReference/CommonErrors.html) : Client and server errors that all operations can return.

If youâre new to Audit Manager, we recommend that you review the [Audit Manager User Guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) .

## Available Commands

- [associate-assessment-report-evidence-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/associate-assessment-report-evidence-folder.html)
- [batch-associate-assessment-report-evidence](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-associate-assessment-report-evidence.html)
- [batch-create-delegation-by-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-create-delegation-by-assessment.html)
- [batch-delete-delegation-by-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-delete-delegation-by-assessment.html)
- [batch-disassociate-assessment-report-evidence](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-disassociate-assessment-report-evidence.html)
- [batch-import-evidence-to-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-import-evidence-to-assessment-control.html)
- [create-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/create-assessment.html)
- [create-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/create-assessment-framework.html)
- [create-assessment-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/create-assessment-report.html)
- [create-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/create-control.html)
- [delete-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment.html)
- [delete-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment-framework.html)
- [delete-assessment-framework-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment-framework-share.html)
- [delete-assessment-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-assessment-report.html)
- [delete-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/delete-control.html)
- [deregister-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/deregister-account.html)
- [deregister-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/deregister-organization-admin-account.html)
- [disassociate-assessment-report-evidence-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/disassociate-assessment-report-evidence-folder.html)
- [get-account-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-account-status.html)
- [get-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment.html)
- [get-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-framework.html)
- [get-assessment-report-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-assessment-report-url.html)
- [get-change-logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-change-logs.html)
- [get-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-control.html)
- [get-delegations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-delegations.html)
- [get-evidence](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence.html)
- [get-evidence-by-evidence-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-by-evidence-folder.html)
- [get-evidence-file-upload-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-file-upload-url.html)
- [get-evidence-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-folder.html)
- [get-evidence-folders-by-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-folders-by-assessment.html)
- [get-evidence-folders-by-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-folders-by-assessment-control.html)
- [get-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-insights.html)
- [get-insights-by-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-insights-by-assessment.html)
- [get-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-organization-admin-account.html)
- [get-services-in-scope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-services-in-scope.html)
- [get-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-settings.html)
- [list-assessment-control-insights-by-control-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-control-insights-by-control-domain.html)
- [list-assessment-framework-share-requests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-framework-share-requests.html)
- [list-assessment-frameworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-frameworks.html)
- [list-assessment-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessment-reports.html)
- [list-assessments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html)
- [list-control-domain-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-control-domain-insights.html)
- [list-control-domain-insights-by-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-control-domain-insights-by-assessment.html)
- [list-control-insights-by-control-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-control-insights-by-control-domain.html)
- [list-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-controls.html)
- [list-keywords-for-data-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-keywords-for-data-source.html)
- [list-notifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-notifications.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-tags-for-resource.html)
- [register-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/register-account.html)
- [register-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/register-organization-admin-account.html)
- [start-assessment-framework-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/start-assessment-framework-share.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/untag-resource.html)
- [update-assessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment.html)
- [update-assessment-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control.html)
- [update-assessment-control-set-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-control-set-status.html)
- [update-assessment-framework](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-framework.html)
- [update-assessment-framework-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-framework-share.html)
- [update-assessment-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-status.html)
- [update-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-control.html)
- [update-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-settings.html)
- [validate-assessment-report-integrity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/validate-assessment-report-integrity.html)