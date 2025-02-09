import re

from cc.settings import NODES


def get_next_nodes(current_node_id: str):
    clean_node_id = re.sub(r"[^ABCDE]", "", current_node_id)
    return [f"{clean_node_id}{i}" for i in NODES]


def get_depth(node_id: str):
    node_id = re.sub(r"[^ABCDE]", "", node_id)
    return len(node_id)
