import boto3
import pandas as pd
import numpy as np
from d3graph import d3graph


def generate_graph(adjmat):
    d3 = d3graph()
    d3.graph(adjmat)
    d3.save("graph.html")
    d3.show()


def get_resources(aws_account_id, aws_region):
    """
    Function to interact with AWS Quicksight using Boto3.
    It gets all the AWS Quicksight resources and their dependencies
    and returns them in a format that can be used by D3Graph.
    """
    client = boto3.client("quicksight")

    resources = {
        "Analyses": client.list_analyses(AwsAccountId=aws_account_id),
        "Dashboards": client.list_dashboards(AwsAccountId=aws_account_id),
        "DataSets": client.list_data_sets(AwsAccountId=aws_account_id),
        "DataSources": client.list_data_sources(AwsAccountId=aws_account_id),
        "RefreshSchedules": client.list_ingestions(
            DataSetId=aws_account_id, AwsAccountId=aws_account_id
        ),
        "Themes": client.list_themes(AwsAccountId=aws_account_id),
        "VPCConnections": client.list_vpc_connection(AwsAccountId=aws_account_id),
    }

    # Create an adjacency matrix
    resource_names = list(resources.keys())
    adjacency_matrix = pd.DataFrame(
        np.zeros((len(resource_names), len(resource_names))),
        index=resource_names,
        columns=resource_names,
    )

    # Fill the adjacency matrix
    for resource_name, resource_data in resources.items():
        for dependency in resource_data:
            if dependency in resource_names:
                adjacency_matrix.loc[resource_name, dependency] = 1

    return adjacency_matrix


def get_member_resources():
    """
    Function to interact with AWS Quicksight using Boto3.
    It gets all the AWS Quicksight resources and their nested dependencies
    and returns them in a format that can be used by D3Graph.
    """
    client = boto3.client("quicksight")

    # List all AWS QuickSight resources
    response = client.list_user_groups(
        AwsAccountId="string", Namespace="string", UserName="string"
    )

    # Get nested dependencies
    nested_dependencies = {}
    for group in response["GroupList"]:
        nested_dependencies[group["GroupName"]] = client.list_group_memberships(
            AwsAccountId="string", Namespace="string", GroupName=group["GroupName"]
        )

    # Format data for D3Graph
    formatted_data = []
    for group, members in nested_dependencies.items():
        formatted_data.append(
            {
                "name": group,
                "children": [
                    {"name": member["MemberName"]} for member in members["MemberList"]
                ],
            }
        )

    return formatted_data
