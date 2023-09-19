import boto3


def get_resources():
    return None


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
