# elbv2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# elbv2

## Description

A load balancer distributes incoming traffic across targets, such as your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered targets and ensures that it routes traffic only to healthy targets. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer. You configure a target group with a protocol and port number for connections from the load balancer to the targets, and with health check settings to be used when checking the health status of the targets.

Elastic Load Balancing supports the following types of load balancers: Application Load Balancers, Network Load Balancers, Gateway Load Balancers, and Classic Load Balancers. This reference covers the following load balancer types:

- Application Load Balancer - Operates at the application layer (layer 7) and supports HTTP and HTTPS.
- Network Load Balancer - Operates at the transport layer (layer 4) and supports TCP, TLS, and UDP.
- Gateway Load Balancer - Operates at the network layer (layer 3).

For more information, see the [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) .

All Elastic Load Balancing operations are idempotent, which means that they complete at most one time. If you repeat an operation, it succeeds.

## Available Commands

- [add-listener-certificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-listener-certificates.html)
- [add-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-tags.html)
- [add-trust-store-revocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-trust-store-revocations.html)
- [create-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html)
- [create-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-load-balancer.html)
- [create-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-rule.html)
- [create-target-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html)
- [create-trust-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-trust-store.html)
- [delete-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-listener.html)
- [delete-load-balancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-load-balancer.html)
- [delete-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-rule.html)
- [delete-shared-trust-store-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-shared-trust-store-association.html)
- [delete-target-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-target-group.html)
- [delete-trust-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-trust-store.html)
- [deregister-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/deregister-targets.html)
- [describe-account-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-account-limits.html)
- [describe-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-capacity-reservation.html)
- [describe-listener-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-attributes.html)
- [describe-listener-certificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-certificates.html)
- [describe-listeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listeners.html)
- [describe-load-balancer-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancer-attributes.html)
- [describe-load-balancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancers.html)
- [describe-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html)
- [describe-ssl-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-ssl-policies.html)
- [describe-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-tags.html)
- [describe-target-group-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-group-attributes.html)
- [describe-target-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-groups.html)
- [describe-target-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-health.html)
- [describe-trust-store-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-trust-store-associations.html)
- [describe-trust-store-revocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-trust-store-revocations.html)
- [describe-trust-stores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-trust-stores.html)
- [get-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/get-resource-policy.html)
- [get-trust-store-ca-certificates-bundle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/get-trust-store-ca-certificates-bundle.html)
- [get-trust-store-revocation-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/get-trust-store-revocation-content.html)
- [modify-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-capacity-reservation.html)
- [modify-ip-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-ip-pools.html)
- [modify-listener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener.html)
- [modify-listener-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener-attributes.html)
- [modify-load-balancer-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-load-balancer-attributes.html)
- [modify-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-rule.html)
- [modify-target-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group.html)
- [modify-target-group-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group-attributes.html)
- [modify-trust-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-trust-store.html)
- [register-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/register-targets.html)
- [remove-listener-certificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-listener-certificates.html)
- [remove-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-tags.html)
- [remove-trust-store-revocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-trust-store-revocations.html)
- [set-ip-address-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-ip-address-type.html)
- [set-rule-priorities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-rule-priorities.html)
- [set-security-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-security-groups.html)
- [set-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-subnets.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/wait/index.html)