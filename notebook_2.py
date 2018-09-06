def normalize_string(s):
    assert type (s) is str
    return ''.join([c for c in s.lower() if c.isalpha() or c.isspace()])

def get_normalized_words (s):
    assert type (s) is str
    return normalize_string(s).split()

def make_itemsets(words):
    return [set(word) for word in words]

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict
    for a,b in combinations(itemset,2):
        pair_counts[(a,b)] +=1
        pair_counts[(b,a)] +=1

def update_item_counts(item_counts, itemset):
    for a in itemset:
        item_counts[a] +=1

def filter_rules_by_conf (pair_counts, item_counts, threshold):
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    for (a,b) in pair_counts:
        assert a in item_counts
        conf_ab = pair_counts[(a,b)] / item_counts[a]
        if conf_ab >= threshold:
            rules[(a,b)] = conf_ab
    return rules

def find_assoc_rules(receipts, threshold):
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)
    for itemset in receipts:
        update_pair_counts(pair_counts, itemset)
        update_item_counts(item_counts, itemset)
    rules = filter_rules_by_conf(pair_counts, item_counts, threshold)
    return rules


latin_words = get_normalized_words(latin_text)
latin_itemsets = make_itemsets(latin_words)
latin_rules = find_assoc_rules(latin_itemsets, 0.75)

def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict
    common = []
    for item in d1.keys():
        if item in d2.keys():
            common.append(item)
    return common

english_words = get_normalized_words(english_text)
english_itemsets = make_itemsets(english_words)
english_rules = find_assoc_rules(english_itemsets, 0.75)
common_high_conf_rules = intersect_keys(english_rules, latin_rules)
# Inspect your result:
print("High-confidence rules common to _lorem ipsum_ in Latin and English:")
print_rules(common_high_conf_rules)


# create an itemsets [{item1,item2}, {item1, item3, item5}, ...]
itemsets = []
customers_groceries = groceries_file.split("\n")
for customer_groceries in customers_groceries:
    items = customer_groceries.split(",")
    itemsets.append(set(items))
# calculate item_counts
pair_counts = defaultdict(int)
item_counts = defaultdict(int)
for itemset in itemsets:
    update_item_counts(item_counts, itemset)
    update_pair_counts(pair_counts, itemset)
# remove items whoes counts are less than MIN_COUNT
item_counts_copy = item_counts.copy()
for key in item_counts_copy.keys():
    if item_counts_copy[key] < MIN_COUNT:
        del item_counts[key]
# remove pairs whoes items are removed in the previous step
pair_counts_copy = pair_counts.copy()
for (a,b) in pair_counts_copy.keys():
    if (a not in item_counts.keys()) or (b not in item_counts.keys()):
        del pair_counts[(a,b)]
# calculate assoc rules
basket_rules = filter_rules_by_conf(pair_counts, item_counts, THRESHOLD)
