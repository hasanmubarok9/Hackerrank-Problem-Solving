# Complete the workbook function below.
import math


def workbook(n, k, arr):
    # naive solution

    # find page needed for every chapter
    total_pages = sum([math.floor(problem / k) + math.ceil((problem %
                                                            k) / k) if problem > k else 1 for problem in arr])

    # create dictionary to mapping list to every page
    pages = dict((key, []) for key in range(1, total_pages + 1))

    page_counter = 1
    while page_counter <= total_pages:
        for problem in arr:
            problems = [index for index in range(1, problem + 1)]
            for item in problems:
                if len(pages[page_counter]) < k:
                    pages[page_counter].append(item)
                else:
                    page_counter += 1
                    pages[page_counter].append(item)
            page_counter += 1

    special_problems = sum(
        [1 if key in pages[key] else 0 for key in pages.keys()])

    return special_problems
