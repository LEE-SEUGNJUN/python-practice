##딕셔너리로 변수를 만들고 입력한 key값에 따른 value값 나오게하기
##변수선언##
animal = {"닭" : "병아리",     ## 인터넷 검색하여 새끼이름을 알아내어
          "개" : "강아지",     ## 딕셔너리 형태로 변수선언하였다
          "곰" : "능소니",
          "고등어" : "고도리",
          "명태" : "노가리",
          "말" : "망아지",
          "호랑이" : "개호주"}

##메인코드 부분##
if __name__ == "__main__" :  ##main 함수와 같은 역할 
    while(True) : ##무한반복
        myanimal = input(str(list(animal.keys())) + " 중 새끼 이름을 알고싶은 동물은 ? : ") ##딕셔너리변수를 리스트,문자열처리하여
        if myanimal in animal :## animal 변수안에 내가 입력한 이름이 있으면.                   input 문구에 보이게 하였다
            print("%s의 새끼 이름은 %s 입니다. " % (myanimal,animal.get(myanimal))) ## 내가입력한동물의 새끼이름은
        elif myanimal == "끝" : ##끝을 입력하면 반복문 종료                          ## get()함수를이용하여 value값을 끌어냈다
            break
        else : ## 이외에 다른 문자를 입력하면 다시 입력하라는 문구 출력
            print("잘못 입력하셨습니다 다시 입력하세요.")

