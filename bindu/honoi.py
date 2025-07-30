def tower_of_hanoi(disk,source,auxilary,target):
    if disk==1:
        print("move disk 1 from rod {}.". format(source,target))
        return
    tower_of_hanoi(disk-1,source,target,auxilary)
    print("move disk{} from rod {} to rod{}.".
format(disk,source,target))
    tower_of_hanoi(disk-1,auxilary,source,target)
disk=int(input("enter the number of disks:"))
tower_of_hanoi(disk,'a','b','c')
