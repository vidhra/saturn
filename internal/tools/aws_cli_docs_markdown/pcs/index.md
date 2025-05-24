# pcsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# pcs

## Description

Amazon Web Services Parallel Computing Service (Amazon Web Services PCS) is a managed service that makes it easier for you to run and scale your high performance computing (HPC) workloads, and build scientific and engineering models on Amazon Web Services using Slurm. For more information, see the [Amazon Web Services Parallel Computing Service User Guide](https://docs.aws.amazon.com/pcs/latest/userguide) .

This reference describes the actions and data types of the service management API. You can use the Amazon Web Services SDKs to call the API actions in software, or use the Command Line Interface (CLI) to call the API actions manually. These API actions manage the service through an Amazon Web Services account.

The API actions operate on Amazon Web Services PCS resources. A *resource* is an entity in Amazon Web Services that you can work with. Amazon Web Services services create resources when you use the features of the service. Examples of Amazon Web Services PCS resources include clusters, compute node groups, and queues. For more information about resources in Amazon Web Services, see [Resource](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-terms-and-concepts.html#term-resource) in the *Resource Explorer User Guide* .

An Amazon Web Services PCS *compute node* is an Amazon EC2 instance. You donât launch compute nodes directly. Amazon Web Services PCS uses configuration information that you provide to launch compute nodes in your Amazon Web Services account. You receive billing charges for your running compute nodes. Amazon Web Services PCS automatically terminates your compute nodes when you delete the Amazon Web Services PCS resources related to those compute nodes.

## Available Commands

- [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/create-cluster.html)
- [create-compute-node-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/create-compute-node-group.html)
- [create-queue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/create-queue.html)
- [delete-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/delete-cluster.html)
- [delete-compute-node-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/delete-compute-node-group.html)
- [delete-queue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/delete-queue.html)
- [get-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-cluster.html)
- [get-compute-node-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-compute-node-group.html)
- [get-queue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-queue.html)
- [list-clusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/list-clusters.html)
- [list-compute-node-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/list-compute-node-groups.html)
- [list-queues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/list-queues.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/list-tags-for-resource.html)
- [register-compute-node-group-instance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/register-compute-node-group-instance.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/untag-resource.html)
- [update-compute-node-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/update-compute-node-group.html)
- [update-queue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/update-queue.html)