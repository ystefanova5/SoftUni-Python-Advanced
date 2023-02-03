from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
paper_pieces = deque([int(x) for x in input().split(", ")])
box_size = 50
filled_boxes = 0

while eggs and paper_pieces:
    egg = eggs.popleft()

    if egg <= 0:
        continue
    elif egg == 13:
        first_paper_piece = paper_pieces.popleft()
        last_paper_piece = paper_pieces.pop()
        paper_pieces.appendleft(last_paper_piece)
        paper_pieces.append(first_paper_piece)
        continue

    paper = paper_pieces.pop()
    if egg + paper <= box_size:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")

if paper_pieces:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_pieces])}")
