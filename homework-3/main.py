import sys
from src.channel import Channel


if __name__ == '__main__':
    #sys.getrecursionlimit(1000)
    # Создаем два экземпляра класса
    redactsiya = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # Используем различные магические методы
    print(vdud)  # 'вДудь (https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA)'
    print(vdud + redactsiya)  # 13970000
    print(vdud - redactsiya)  # 6630000
    print(redactsiya - vdud)  # -6630000
    print(vdud > redactsiya)  # True
    print(vdud >= redactsiya)  # True
    print(vdud < redactsiya)  # False
    print(vdud <= redactsiya)  # False
    print(vdud == redactsiya)  # False
    
