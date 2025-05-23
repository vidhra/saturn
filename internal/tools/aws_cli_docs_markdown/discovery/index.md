# discoveryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# discovery

## Description

Amazon Web Services Application Discovery Service (Application Discovery Service) helps you plan application migration projects. It automatically identifies servers, virtual machines (VMs), and network dependencies in your on-premises data centers. For more information, see the [Amazon Web Services Application Discovery Service FAQ](http://aws.amazon.com/application-discovery/faqs/) .

Application Discovery Service offers three ways of performing discovery and collecting data about your on-premises servers:

- **Agentless discovery** using Amazon Web Services Application Discovery Service Agentless Collector (Agentless Collector), which doesnât require you to install an agent on each host.
- Agentless Collector gathers server information regardless of the operating systems, which minimizes the time required for initial on-premises infrastructure assessment.
- Agentless Collector doesnât collect information about network dependencies, only agent-based discovery collects that information.
- **Agent-based discovery** using the Amazon Web Services Application Discovery Agent (Application Discovery Agent) collects a richer set of data than agentless discovery, which you install on one or more hosts in your data center.
- The agent captures infrastructure and application information, including an inventory of running processes, system performance information, resource utilization, and network dependencies.
- The information collected by agents is secured at rest and in transit to the Application Discovery Service database in the Amazon Web Services cloud. For more information, see [Amazon Web Services Application Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) .
- **Amazon Web Services Partner Network (APN) solutions** integrate with Application Discovery Service, enabling you to import details of your on-premises environment directly into Amazon Web Services Migration Hub (Migration Hub) without using Agentless Collector or Application Discovery Agent.
- Third-party application discovery tools can query Amazon Web Services Application Discovery Service, and they can write to the Application Discovery Service database using the public API.
- In this way, you can import data into Migration Hub and view it, so that you can associate applications with servers and track migrations.

**Working With This Guide**

This API reference provides descriptions, syntax, and usage examples for each of the actions and data types for Application Discovery Service. The topic for each action shows the API request parameters and the response. Alternatively, you can use one of the Amazon Web Services SDKs to access an API that is tailored to the programming language or platform that youâre using. For more information, see [Amazon Web Services SDKs](http://aws.amazon.com/tools/#SDKs) .

### Note

- Remember that you must set your Migration Hub home Region before you call any of these APIs.
- You must make API calls for write actions (create, notify, associate, disassociate, import, or put) while in your home Region, or a `HomeRegionNotSetException` error is returned.
- API calls for read actions (list, describe, stop, and delete) are permitted outside of your home Region.
- Although it is unlikely, the Migration Hub home Region could change. If you call APIs outside the home Region, an `InvalidInputException` is returned.
- You must call `GetHomeRegion` to obtain the latest Migration Hub home Region.

This guide is intended for use with the [Amazon Web Services Application Discovery Service User Guide](https://docs.aws.amazon.com/application-discovery/latest/userguide/) .

### Warning

All data is handled according to the [Amazon Web Services Privacy Policy](https://aws.amazon.com/privacy/) . You can operate Application Discovery Service offline to inspect collected data before it is shared with the service.

## Available Commands

- [associate-configuration-items-to-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/associate-configuration-items-to-application.html)
- [batch-delete-agents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/batch-delete-agents.html)
- [batch-delete-import-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/batch-delete-import-data.html)
- [create-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/create-application.html)
- [create-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/create-tags.html)
- [delete-applications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/delete-applications.html)
- [delete-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/delete-tags.html)
- [describe-agents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-agents.html)
- [describe-batch-delete-configuration-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-batch-delete-configuration-task.html)
- [describe-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-configurations.html)
- [describe-continuous-exports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-continuous-exports.html)
- [describe-export-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-export-tasks.html)
- [describe-import-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-import-tasks.html)
- [describe-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-tags.html)
- [disassociate-configuration-items-from-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/disassociate-configuration-items-from-application.html)
- [get-discovery-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/get-discovery-summary.html)
- [list-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/list-configurations.html)
- [list-server-neighbors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/list-server-neighbors.html)
- [start-batch-delete-configuration-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-batch-delete-configuration-task.html)
- [start-continuous-export](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-continuous-export.html)
- [start-data-collection-by-agent-ids](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-data-collection-by-agent-ids.html)
- [start-export-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-export-task.html)
- [start-import-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-import-task.html)
- [stop-continuous-export](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/stop-continuous-export.html)
- [stop-data-collection-by-agent-ids](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/stop-data-collection-by-agent-ids.html)
- [update-application](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/update-application.html)