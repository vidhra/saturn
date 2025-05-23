# managedblockchainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# managedblockchain

## Description

Amazon Managed Blockchain is a fully managed service for creating and managing blockchain networks using open-source frameworks. Blockchain allows you to build applications where multiple parties can securely and transparently run transactions and share data without the need for a trusted, central authority.

Managed Blockchain supports the Hyperledger Fabric and Ethereum open-source frameworks. Because of fundamental differences between the frameworks, some API actions or data types may only apply in the context of one framework and not the other. For example, actions related to Hyperledger Fabric network members such as `CreateMember` and `DeleteMember` donât apply to Ethereum.

The description for each action indicates the framework or frameworks to which it applies. Data types and properties that apply only in the context of a particular framework are similarly indicated.

## Available Commands

- [create-accessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-accessor.html)
- [create-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-member.html)
- [create-network](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-network.html)
- [create-node](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-node.html)
- [create-proposal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/create-proposal.html)
- [delete-accessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-accessor.html)
- [delete-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-member.html)
- [delete-node](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/delete-node.html)
- [get-accessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-accessor.html)
- [get-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-member.html)
- [get-network](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-network.html)
- [get-node](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html)
- [get-proposal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-proposal.html)
- [list-accessors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-accessors.html)
- [list-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-invitations.html)
- [list-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html)
- [list-networks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-networks.html)
- [list-nodes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-nodes.html)
- [list-proposal-votes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposal-votes.html)
- [list-proposals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposals.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-tags-for-resource.html)
- [reject-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/reject-invitation.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/untag-resource.html)
- [update-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-member.html)
- [update-node](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/update-node.html)
- [vote-on-proposal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/vote-on-proposal.html)