# redshiftÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# redshift

## Description

**Overview**

This is an interface reference for Amazon Redshift. It contains documentation for one of the programming or command line interfaces you can use to manage Amazon Redshift clusters. Note that Amazon Redshift is asynchronous, which means that some interfaces may require techniques, such as polling or asynchronous callback handlers, to determine when a command has been applied. In this reference, the parameter descriptions indicate whether a change is applied immediately, on the next instance reboot, or during the next maintenance window. For a summary of the Amazon Redshift cluster management interfaces, go to [Using the Amazon Redshift Management Interfaces](https://docs.aws.amazon.com/redshift/latest/mgmt/using-aws-sdk.html) .

Amazon Redshift manages all the work of setting up, operating, and scaling a data warehouse: provisioning capacity, monitoring and backing up the cluster, and applying patches and upgrades to the Amazon Redshift engine. You can focus on using your data to acquire new insights for your business and customers.

If you are a first-time user of Amazon Redshift, we recommend that you begin by reading the [Amazon Redshift Getting Started Guide](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) .

If you are a database developer, the [Amazon Redshift Database Developer Guide](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html) explains how to design, build, query, and maintain the databases that make up your data warehouse.

## Available Commands

- [accept-reserved-node-exchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/accept-reserved-node-exchange.html)
- [add-partner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/add-partner.html)
- [associate-data-share-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/associate-data-share-consumer.html)
- [authorize-cluster-security-group-ingress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-cluster-security-group-ingress.html)
- [authorize-data-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-data-share.html)
- [authorize-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-endpoint-access.html)
- [authorize-snapshot-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-snapshot-access.html)
- [batch-delete-cluster-snapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-delete-cluster-snapshots.html)
- [batch-modify-cluster-snapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-modify-cluster-snapshots.html)
- [cancel-resize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/cancel-resize.html)
- [copy-cluster-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/copy-cluster-snapshot.html)
- [create-authentication-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-authentication-profile.html)
- [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html)
- [create-cluster-parameter-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-parameter-group.html)
- [create-cluster-security-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html)
- [create-cluster-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-snapshot.html)
- [create-cluster-subnet-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-subnet-group.html)
- [create-custom-domain-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-custom-domain-association.html)
- [create-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-endpoint-access.html)
- [create-event-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-event-subscription.html)
- [create-hsm-client-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-client-certificate.html)
- [create-hsm-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-configuration.html)
- [create-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-integration.html)
- [create-redshift-idc-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-redshift-idc-application.html)
- [create-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-scheduled-action.html)
- [create-snapshot-copy-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-copy-grant.html)
- [create-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-schedule.html)
- [create-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-tags.html)
- [create-usage-limit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-usage-limit.html)
- [deauthorize-data-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/deauthorize-data-share.html)
- [delete-authentication-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-authentication-profile.html)
- [delete-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html)
- [delete-cluster-parameter-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-parameter-group.html)
- [delete-cluster-security-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-security-group.html)
- [delete-cluster-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-snapshot.html)
- [delete-cluster-subnet-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-subnet-group.html)
- [delete-custom-domain-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-custom-domain-association.html)
- [delete-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-endpoint-access.html)
- [delete-event-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-event-subscription.html)
- [delete-hsm-client-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-client-certificate.html)
- [delete-hsm-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-configuration.html)
- [delete-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-integration.html)
- [delete-partner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-partner.html)
- [delete-redshift-idc-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-redshift-idc-application.html)
- [delete-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-resource-policy.html)
- [delete-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-scheduled-action.html)
- [delete-snapshot-copy-grant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-copy-grant.html)
- [delete-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-schedule.html)
- [delete-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-tags.html)
- [delete-usage-limit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-usage-limit.html)
- [deregister-namespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/deregister-namespace.html)
- [describe-account-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-account-attributes.html)
- [describe-authentication-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-authentication-profiles.html)
- [describe-cluster-db-revisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-db-revisions.html)
- [describe-cluster-parameter-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameter-groups.html)
- [describe-cluster-parameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameters.html)
- [describe-cluster-security-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-security-groups.html)
- [describe-cluster-snapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html)
- [describe-cluster-subnet-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-subnet-groups.html)
- [describe-cluster-tracks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-tracks.html)
- [describe-cluster-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-versions.html)
- [describe-clusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html)
- [describe-custom-domain-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-custom-domain-associations.html)
- [describe-data-shares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-data-shares.html)
- [describe-data-shares-for-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-data-shares-for-consumer.html)
- [describe-data-shares-for-producer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-data-shares-for-producer.html)
- [describe-default-cluster-parameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-default-cluster-parameters.html)
- [describe-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-endpoint-access.html)
- [describe-endpoint-authorization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-endpoint-authorization.html)
- [describe-event-categories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-categories.html)
- [describe-event-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-subscriptions.html)
- [describe-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-events.html)
- [describe-hsm-client-certificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-client-certificates.html)
- [describe-hsm-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-configurations.html)
- [describe-inbound-integrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-inbound-integrations.html)
- [describe-integrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-integrations.html)
- [describe-logging-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-logging-status.html)
- [describe-node-configuration-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-node-configuration-options.html)
- [describe-orderable-cluster-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-orderable-cluster-options.html)
- [describe-partners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-partners.html)
- [describe-redshift-idc-applications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-redshift-idc-applications.html)
- [describe-reserved-node-exchange-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-node-exchange-status.html)
- [describe-reserved-node-offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-node-offerings.html)
- [describe-reserved-nodes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-nodes.html)
- [describe-resize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-resize.html)
- [describe-scheduled-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html)
- [describe-snapshot-copy-grants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-copy-grants.html)
- [describe-snapshot-schedules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-schedules.html)
- [describe-storage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-storage.html)
- [describe-table-restore-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-table-restore-status.html)
- [describe-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-tags.html)
- [describe-usage-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-usage-limits.html)
- [disable-logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-logging.html)
- [disable-snapshot-copy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-snapshot-copy.html)
- [disassociate-data-share-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disassociate-data-share-consumer.html)
- [enable-logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-logging.html)
- [enable-snapshot-copy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-snapshot-copy.html)
- [failover-primary-compute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/failover-primary-compute.html)
- [get-cluster-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials.html)
- [get-cluster-credentials-with-iam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials-with-iam.html)
- [get-reserved-node-exchange-configuration-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-reserved-node-exchange-configuration-options.html)
- [get-reserved-node-exchange-offerings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-reserved-node-exchange-offerings.html)
- [get-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-resource-policy.html)
- [list-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/list-recommendations.html)
- [modify-aqua-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-aqua-configuration.html)
- [modify-authentication-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-authentication-profile.html)
- [modify-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html)
- [modify-cluster-db-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-db-revision.html)
- [modify-cluster-iam-roles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-iam-roles.html)
- [modify-cluster-maintenance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-maintenance.html)
- [modify-cluster-parameter-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-parameter-group.html)
- [modify-cluster-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html)
- [modify-cluster-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot-schedule.html)
- [modify-cluster-subnet-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-subnet-group.html)
- [modify-custom-domain-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-custom-domain-association.html)
- [modify-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-endpoint-access.html)
- [modify-event-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-event-subscription.html)
- [modify-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-integration.html)
- [modify-redshift-idc-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-redshift-idc-application.html)
- [modify-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-scheduled-action.html)
- [modify-snapshot-copy-retention-period](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-copy-retention-period.html)
- [modify-snapshot-schedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-schedule.html)
- [modify-usage-limit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-usage-limit.html)
- [pause-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/pause-cluster.html)
- [purchase-reserved-node-offering](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/purchase-reserved-node-offering.html)
- [put-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/put-resource-policy.html)
- [reboot-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html)
- [register-namespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/register-namespace.html)
- [reject-data-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reject-data-share.html)
- [reset-cluster-parameter-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html)
- [resize-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resize-cluster.html)
- [restore-from-cluster-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html)
- [restore-table-from-cluster-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-table-from-cluster-snapshot.html)
- [resume-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resume-cluster.html)
- [revoke-cluster-security-group-ingress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-cluster-security-group-ingress.html)
- [revoke-endpoint-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-endpoint-access.html)
- [revoke-snapshot-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-snapshot-access.html)
- [rotate-encryption-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/rotate-encryption-key.html)
- [update-partner-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/update-partner-status.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/wait/index.html)