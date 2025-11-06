from pyvis.network import Network

# ソート

subjects_sorted = sorted(subjects)

# ノード管理

node_map = {}  # path -> node_id

node_id = 0

node_children_count = {}  # node_id -> 子の数

# Network作成

net = Network(height="800px", width="100%", directed=True, notebook=False)

# 前回の共通接頭辞

prev_common = ""

# 2つずつ処理

for i in range(len(subjects_sorted)):

    subj1 = subjects_sorted[i]

    subj2 = subjects_sorted[i + 1] if i + 1 < len(subjects_sorted) else ""

    # 共通接頭辞を見つける

    common = ""

    for j in range(min(len(subj1), len(subj2))):

        if subj1[j] == subj2[j]:

            common += subj1[j]

        else:

            break

    # subj1をツリーに追加

    if subj1 not in node_map:

        # 親を決定

        if prev_common and subj1.startswith(prev_common):

            parent_path = prev_common

        else:

            # 遡り: subj1とprev_commonの共通部分

            temp_common = ""

            for j in range(min(len(subj1), len(prev_common))):

                if subj1[j] == prev_common[j]:

                    temp_common += subj1[j]

                else:

                    break

            parent_path = temp_common

        # 親ノードを確保

        if parent_path and parent_path not in node_map:

            parent_id = node_id

            node_id += 1

            node_map[parent_path] = parent_id

            node_children_count[parent_id] = 0

            net.add_node(
                parent_id,
                label=parent_path,
                title=parent_path,
                color="lightblue",
                size=10,
            )

        # subj1ノード追加

        curr_id = node_id

        node_id += 1

        node_map[subj1] = curr_id

        node_children_count[curr_id] = 0

        label = subj1[len(parent_path) :] if parent_path else subj1

        net.add_node(curr_id, label=label, title=subj1, color="lightgreen", size=10)

        # エッジ追加と親の子カウント増加

        if parent_path:

            parent_id = node_map[parent_path]

            net.add_edge(parent_id, curr_id)

            node_children_count[parent_id] += 1

    # 最後のペア処理

    if subj2 and subj2 not in node_map:

        # subj2の親はcommon

        if common and common not in node_map:

            parent_id = node_id

            node_id += 1

            node_map[common] = parent_id

            node_children_count[parent_id] = 0

            net.add_node(
                parent_id, label=common, title=common, color="lightblue", size=10
            )

        curr_id = node_id

        node_id += 1

        node_map[subj2] = curr_id

        node_children_count[curr_id] = 0

        label = subj2[len(common) :] if common else subj2

        net.add_node(curr_id, label=label, title=subj2, color="lightgreen", size=10)

        if common:

            parent_id = node_map[common]

            net.add_edge(parent_id, curr_id)

            node_children_count[parent_id] += 1

    prev_common = common

# サイズを更新（子の数に応じて）

for nid in node_children_count:

    count = node_children_count[nid]

    if count > 0:

        new_size = 5 + count * 10  # 基本サイズ10 + 子1つにつき3

        net.get_node(nid)["size"] = new_size

        net.get_node(nid)["value"] = new_size

# HTML出力

net.save_graph("subjects_tree.html")
