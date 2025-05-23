# globalacceleratorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# globalaccelerator

## Description

This is the *Global Accelerator API Reference* . This guide is for developers who need detailed information about Global Accelerator API actions, data types, and errors. For more information about Global Accelerator features, see the [Global Accelerator Developer Guide](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) .

Global Accelerator is a service in which you create *accelerators* to improve the performance of your applications for local and global users. Depending on the type of accelerator you choose, you can gain additional benefits.

- By using a standard accelerator, you can improve availability of your internet applications that are used by a global audience. With a standard accelerator, Global Accelerator directs traffic to optimal endpoints over the Amazon Web Services global network.
- For other scenarios, you might choose a custom routing accelerator. With a custom routing accelerator, you can use application logic to directly map one or more users to a specific endpoint among many endpoints.

### Warning

Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify `--region us-west-2` on Amazon Web Services CLI commands.

By default, Global Accelerator provides you with static IP addresses that you associate with your accelerator. The static IP addresses are anycast from the Amazon Web Services edge network. For IPv4, Global Accelerator provides two static IPv4 addresses. For dual-stack, Global Accelerator provides a total of four addresses: two static IPv4 addresses and two static IPv6 addresses. With a standard accelerator for IPv4, instead of using the addresses that Global Accelerator provides, you can configure these entry points to be IPv4 addresses from your own IP address ranges that you bring to Global Accelerator (BYOIP).

For a standard accelerator, they distribute incoming application traffic across multiple endpoint resources in multiple Amazon Web Services Regions , which increases the availability of your applications. Endpoints for standard accelerators can be Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic IP addresses that are located in one Amazon Web Services Region or multiple Amazon Web Services Regions. For custom routing accelerators, you map traffic that arrives to the static IP addresses to specific Amazon EC2 servers in endpoints that are virtual private cloud (VPC) subnets.

### Warning

The static IP addresses remain assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you *delete* an accelerator, you lose the static IP addresses that are assigned to it, so you can no longer route traffic by using them. You can use IAM policies like tag-based permissions with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see [Tag-based policies](https://docs.aws.amazon.com/global-accelerator/latest/dg/access-control-manage-access-tag-policies.html) .

For standard accelerators, Global Accelerator uses the Amazon Web Services global network to route traffic to the optimal regional endpoint based on health, client location, and policies that you configure. The service reacts instantly to changes in health or configuration to ensure that internet traffic from clients is always directed to healthy endpoints.

For more information about understanding and using Global Accelerator, see the [Global Accelerator Developer Guide](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) .

## Available Commands

- [add-custom-routing-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/add-custom-routing-endpoints.html)
- [add-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/add-endpoints.html)
- [advertise-byoip-cidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/advertise-byoip-cidr.html)
- [allow-custom-routing-traffic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/allow-custom-routing-traffic.html)
- [create-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-accelerator.html)
- [create-cross-account-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-cross-account-attachment.html)
- [create-custom-routing-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-accelerator.html)
- [create-custom-routing-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-endpoint-group.html)
- [create-custom-routing-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-listener.html)
- [create-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html)
- [create-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-listener.html)
- [delete-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-accelerator.html)
- [delete-cross-account-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-cross-account-attachment.html)
- [delete-custom-routing-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-custom-routing-accelerator.html)
- [delete-custom-routing-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-custom-routing-endpoint-group.html)
- [delete-custom-routing-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-custom-routing-listener.html)
- [delete-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-endpoint-group.html)
- [delete-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-listener.html)
- [deny-custom-routing-traffic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/deny-custom-routing-traffic.html)
- [deprovision-byoip-cidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/deprovision-byoip-cidr.html)
- [describe-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-accelerator.html)
- [describe-accelerator-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-accelerator-attributes.html)
- [describe-cross-account-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-cross-account-attachment.html)
- [describe-custom-routing-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-accelerator.html)
- [describe-custom-routing-accelerator-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-accelerator-attributes.html)
- [describe-custom-routing-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-endpoint-group.html)
- [describe-custom-routing-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-listener.html)
- [describe-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-endpoint-group.html)
- [describe-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-listener.html)
- [list-accelerators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-accelerators.html)
- [list-byoip-cidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-byoip-cidrs.html)
- [list-cross-account-attachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-cross-account-attachments.html)
- [list-cross-account-resource-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-cross-account-resource-accounts.html)
- [list-cross-account-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-cross-account-resources.html)
- [list-custom-routing-accelerators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-accelerators.html)
- [list-custom-routing-endpoint-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-endpoint-groups.html)
- [list-custom-routing-listeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-listeners.html)
- [list-custom-routing-port-mappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-port-mappings.html)
- [list-custom-routing-port-mappings-by-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-port-mappings-by-destination.html)
- [list-endpoint-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-endpoint-groups.html)
- [list-listeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-listeners.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-tags-for-resource.html)
- [provision-byoip-cidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/provision-byoip-cidr.html)
- [remove-custom-routing-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/remove-custom-routing-endpoints.html)
- [remove-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/remove-endpoints.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/untag-resource.html)
- [update-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator.html)
- [update-accelerator-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator-attributes.html)
- [update-cross-account-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-cross-account-attachment.html)
- [update-custom-routing-accelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-custom-routing-accelerator.html)
- [update-custom-routing-accelerator-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-custom-routing-accelerator-attributes.html)
- [update-custom-routing-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-custom-routing-listener.html)
- [update-endpoint-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-endpoint-group.html)
- [update-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-listener.html)
- [withdraw-byoip-cidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/withdraw-byoip-cidr.html)