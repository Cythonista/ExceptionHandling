from MyException import *

def main():
    try:
        # 例外の発生を調べる
        f = open('Sample.txt', 'x')
    except FileNotFoundError as e:
        # 例外処理する部分1
        print('Couldn''t open file.')
        print(e)
    except FileExistsError as e:
        # 例外処理する部分2
        print(e)
    except Exception as e:
        print(e)
        raise MyException()
    else:
        # 例外が発生しない時に実行する文
        print('can open file')
        lines = f.readlines()
        for line in lines:
            print(line, end = '')
        f.close()
    finally:
        # 必ず最後に処理
        print('End.')


if __name__ == main():
    main()
