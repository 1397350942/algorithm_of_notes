# def merge(dataset, low, mid, high):
#     i = low
#     j = mid + 1
#     tmp_dataset = []
#     while i <= mid and j <= high:  # 只要左右两边都有数
#         if dataset[i] < dataset[j]:
#             tmp_dataset.append(dataset[i])
#             i += 1
#         if dataset[i] > dataset[j]:
#             tmp_dataset.append(dataset[j])
#             j += 1
#     while i <= mid:  # while执行完毕,肯定有一部分数没了
#         tmp_dataset.append(dataset[i])
#         i += 1
#     while j < high:
#         tmp_dataset.append(dataset[j])
#         j += 1
#     dataset[low:high+1] = tmp_dataset


# if __name__ == "__main__":
#     dataset = [2, 5, 7, 8, 9, 1, 3, 4, 6]
#     print(dataset)
#     merge(dataset, 0, 4, len(dataset)-1)
#     print(dataset)


# def merge(dataset, low, mid, high):
#     i = low
#     j = mid + 1
#     tmp_dataset = []
#     while i <= mid and j <= high:
#         if dataset[i] < dataset[j]:
#             tmp_dataset.append(dataset[i])
#             i += 1
#         if dataset[i] > dataset[j]:
#             tmp_dataset.append(dataset[j])
#             j += 1
#     while i <= mid:
#         tmp_dataset.append(dataset[i])
#         i += 1
#     while j <= high:
#         tmp_dataset.append(dataset[j])
#         j += 1
#     dataset[low:high+1] = tmp_dataset


# if __name__ == "__main__":
#     dataset = [2, 5, 7, 8, 9, 1, 3, 4, 6]
#     print(dataset)
#     merge(dataset, 0, 4, len(dataset)-1)
#     print(dataset)

# def merge(dataset, low, mid, high):
#     """
#     归并
#     """
#     i = low
#     j = mid + 1
#     tmp_dataset = []

#     while i <= mid and j <= high:
#         if dataset[i] < dataset[j]:
#             tmp_dataset.append(dataset[i])
#             i += 1
#         if dataset[i] > dataset[j]:
#             tmp_dataset.append(dataset[j])
#             j += 1
#     while i <= mid:
#         tmp_dataset.append(dataset[i])
#         i += 1
#     while j <= high:
#         tmp_dataset.append(dataset[j])
#         j += 1

#     dataset[low:high+1] = tmp_dataset


# if __name__ == "__main__":
#     dataset = [2, 5, 7, 8, 9, 1, 3, 4, 6]
#     print(dataset)
#     merge(dataset, 0, 4, len(dataset)-1)
#     print(dataset)

def merge(dataset, low, mid, high):
    """
    一次归并
    """
    i = low
    j = mid + 1
    tmp_dataset = []
    while i <= mid and j <= high:
        if dataset[i] < dataset[j]:
            tmp_dataset.append(dataset[i])
            i += 1
        if dataset[i] > dataset[j]:
            tmp_dataset.append(dataset[j])
            j += 1
    while i <= mid:
        tmp_dataset.append(dataset[i])
        i += 1
    while j <= high:
        tmp_dataset.append(dataset[j])
        j += 1
    dataset[low:high+1] = tmp_dataset


if __name__ == "__main__":
    dataset = [2, 5, 7, 8, 9, 1, 3, 4, 6]
    print(dataset)
    merge(dataset, 0, len(dataset)//2, len(dataset)-1)
    print(dataset)
