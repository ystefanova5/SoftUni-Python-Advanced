from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))       # bullets are a stack
locks = deque(list(map(int, input().split())))  # locks are a queue
prize_value = int(input())
shots = 0

while bullets:
    if len(locks) == 0:
        break
    shots += 1
    current_bullet = bullets.pop()
    prize_value -= bullet_price
    if current_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if shots == gun_barrel_size and bullets:
        print("Reloading!")
        shots = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${prize_value}")


################################################   Task Description   ################################################
# 9. *Key Revolver
# Our favorite super-spy action hero Sam is back from his vacation, and it is time to go on a mission. 
# He needs to unlock a safe locked by several locks in a row, which all have varying sizes.
# The hero possesses a special weapon called the Key Revolver, with special bullets. 
# Each bullet can unlock a lock with a size equal to or larger than the size of the bullet. 
# The bullet goes into the keyhole, then explodes, completely destroying it. 
# Sam doesn't know the size of the locks, so he needs to just shoot at all of them until the safe runs out of locks.
# What's behind the safe, you ask? 
# Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, 
# keeps his top-secret Georgian Chacha Brandy recipe inside. 
# It's valued differently across different times of the year, 
# so Sam's boss will tell him what it's worth over the radio. 
# One last thing, every bullet Sam fires will also cost him money, 
# which will be deducted from his pay from the price of the intelligence. 
# Good luck, operative.
# Input
#     • On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
#     • On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
#     • On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
#     • On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
#     • On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
# After Sam receives all of his information and gear (input), 
# he starts to shoot the locks front-to-back while going through the bullets back-to-front.
# If he successfully destroyed a lock, print "Bang!", then remove the lock. 
# If not, print "Ping!", leaving the lock intact. The bullet is removed in both cases.
# If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. 
# If there aren't any bullets left, don't print it.
# The program ends when Sam runs out of bullets or the safe runs out of locks.
# Output
#     • If Sam manages to open the safe, print:
#       "{bullets_left} bullets left. Earned ${money_earned}" 
#     • Otherwise, print:
#       "Couldn't get through. Locks left: {locks_left}"
# Make sure to include the price of the bullets when calculating the money earned.
# Constraints
#     • The input will be within the constraints specified above and will always be valid. 
#       There is no need to check it explicitly.
#     • There will never be a case where Sam breaks the lock and ends up with а negative balance.
