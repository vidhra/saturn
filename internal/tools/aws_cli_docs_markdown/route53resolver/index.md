# route53resolverÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# route53resolver

## Description

When you create a VPC using Amazon VPC, you automatically get DNS resolution within the VPC from Route 53 Resolver. By default, Resolver answers DNS queries for VPC domain names such as domain names for EC2 instances or Elastic Load Balancing load balancers. Resolver performs recursive lookups against public name servers for all other domain names.

You can also configure DNS resolution between your VPC and your network over a Direct Connect or VPN connection:

**Forward DNS queries from resolvers on your network to Route 53 Resolver**

DNS resolvers on your network can forward DNS queries to Resolver in a specified VPC. This allows your DNS resolvers to easily resolve domain names for Amazon Web Services resources such as EC2 instances or records in a Route 53 private hosted zone. For more information, see [How DNS Resolvers on Your Network Forward DNS Queries to Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-network-to-vpc) in the *Amazon Route 53 Developer Guide* .

**Conditionally forward queries from a VPC to resolvers on your network**

You can configure Resolver to forward queries that it receives from EC2 instances in your VPCs to DNS resolvers on your network. To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (example.com, acme.example.com), Resolver chooses the rule with the most specific match (acme.example.com) and forwards the query to the IP addresses that you specified in that rule. For more information, see [How Route 53 Resolver Forwards DNS Queries from Your VPCs to Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-vpc-to-network) in the *Amazon Route 53 Developer Guide* .

Like Amazon VPC, Resolver is Regional. In each Region where you have VPCs, you can choose whether to forward queries from your VPCs to your network (outbound queries), from your network to your VPCs (inbound queries), or both.

## Available Commands

- [associate-firewall-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-firewall-rule-group.html)
- [associate-resolver-endpoint-ip-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-endpoint-ip-address.html)
- [associate-resolver-query-log-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-query-log-config.html)
- [associate-resolver-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html)
- [create-firewall-domain-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-firewall-domain-list.html)
- [create-firewall-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-firewall-rule.html)
- [create-firewall-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-firewall-rule-group.html)
- [create-outpost-resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-outpost-resolver.html)
- [create-resolver-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html)
- [create-resolver-query-log-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-query-log-config.html)
- [create-resolver-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html)
- [delete-firewall-domain-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-firewall-domain-list.html)
- [delete-firewall-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-firewall-rule.html)
- [delete-firewall-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-firewall-rule-group.html)
- [delete-outpost-resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-outpost-resolver.html)
- [delete-resolver-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-endpoint.html)
- [delete-resolver-query-log-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-query-log-config.html)
- [delete-resolver-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html)
- [disassociate-firewall-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-firewall-rule-group.html)
- [disassociate-resolver-endpoint-ip-address](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-endpoint-ip-address.html)
- [disassociate-resolver-query-log-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-query-log-config.html)
- [disassociate-resolver-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html)
- [get-firewall-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-config.html)
- [get-firewall-domain-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-domain-list.html)
- [get-firewall-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-rule-group.html)
- [get-firewall-rule-group-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-rule-group-association.html)
- [get-firewall-rule-group-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-rule-group-policy.html)
- [get-outpost-resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-outpost-resolver.html)
- [get-resolver-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-config.html)
- [get-resolver-dnssec-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-dnssec-config.html)
- [get-resolver-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html)
- [get-resolver-query-log-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config.html)
- [get-resolver-query-log-config-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config-association.html)
- [get-resolver-query-log-config-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config-policy.html)
- [get-resolver-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html)
- [get-resolver-rule-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule-association.html)
- [get-resolver-rule-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule-policy.html)
- [import-firewall-domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/import-firewall-domains.html)
- [list-firewall-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-configs.html)
- [list-firewall-domain-lists](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-domain-lists.html)
- [list-firewall-domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-domains.html)
- [list-firewall-rule-group-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-rule-group-associations.html)
- [list-firewall-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-rule-groups.html)
- [list-firewall-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-rules.html)
- [list-outpost-resolvers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-outpost-resolvers.html)
- [list-resolver-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-configs.html)
- [list-resolver-dnssec-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-dnssec-configs.html)
- [list-resolver-endpoint-ip-addresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoint-ip-addresses.html)
- [list-resolver-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html)
- [list-resolver-query-log-config-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-config-associations.html)
- [list-resolver-query-log-configs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-configs.html)
- [list-resolver-rule-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rule-associations.html)
- [list-resolver-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-tags-for-resource.html)
- [put-firewall-rule-group-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-firewall-rule-group-policy.html)
- [put-resolver-query-log-config-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-resolver-query-log-config-policy.html)
- [put-resolver-rule-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-resolver-rule-policy.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/untag-resource.html)
- [update-firewall-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-config.html)
- [update-firewall-domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-domains.html)
- [update-firewall-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-rule.html)
- [update-firewall-rule-group-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-rule-group-association.html)
- [update-outpost-resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-outpost-resolver.html)
- [update-resolver-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-config.html)
- [update-resolver-dnssec-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-dnssec-config.html)
- [update-resolver-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-endpoint.html)
- [update-resolver-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html)