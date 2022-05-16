# Algorithm_Study
개인적으로 까다로웠던 문제들 모아놓는 곳

------------------------ 2021/07/15 ------------------

LeetCode 5 : Longest Palindromic Substring 가장 긴 팰린드롬 부분 문자열

문제 : https://leetcode.com/problems/longest-palindromic-substring/

풀이 : https://sub2n.github.io/2019/04/22/LeetCode-5-Longest-Palindromic-Substring/


------------------------ 2021/07/25 ------------------

백준 2775 : 부녀회장이 될테야

문제 : https://www.acmicpc.net/problem/2775

풀이 : https://yoonsang-it.tistory.com/12

처음에 재귀함수로 풀어보려 하였으나 시간 초과로 실패했다....

-> 재귀함수 쓸 시간에 리스트로 값 다 저장해놓는게 더 빠른것 같다.

------------------------ 2021/08/01 ------------------

LeetCode 42 : Trapping Rain Water

문제 : https://leetcode.com/problems/trapping-rain-water/

풀이 : https://velog.io/@wind1992/LeetCode-42 

투 포인터를 이용한 풀이가 자주 나오니 잘 알아두면 좋을 것 같고,

또한 스택을 이용한 풀이법이 있는데, 스택을 이용하는 방법에 익숙해져 나가야겠다.

 + 나도 스택을 생각은 했지만, 생각보다 코드로 구현하기가 복잡해서 어려움을 겪었다. 풀이를 계속 보고 알고리즘을 이해하고 넘어가는데 중점을 두기로 하자.

------------------------ 2021/08/05 ------------------

LeetCode 15 : 3Sum

문제 : https://leetcode.com/problems/3sum/

이 역시 투 포인터 유형중 하나인 듯하다. 리스트 내 중복 처리 루틴이 인상깊었다.

------------------------ 2021/08/11 ------------------

LeetCode 238 : Product of Array Except Self

문제 : https://leetcode.com/problems/product-of-array-except-self/

------------------------ 2021/09/13 ------------------

LeetCode 21 : Merge Two Sorted Lists

문제 : https://leetcode.com/problems/merge-two-sorted-lists/

풀이 : https://joecho.tistory.com/entry/leetcode21

책에서는 재귀함수로 풀이해놨는데, 우선 이 풀이부터 이해하고 따라해도 늦지 않을 것 같다.

------------------------ 2021/09/27 ------------------

LeetCode 316 : Remove Duplicate Letters

문제 : https://leetcode.com/problems/remove-duplicate-letters/

풀이 : https://velog.io/@pyh8618/LeetCode-316.-Remove-Duplicate-Letters-%EC%A4%91%EB%B3%B5-%EB%AC%B8%EC%9E%90-%EC%A0%9C%EA%B1%B0

혼자서 해결하려다 안 풀려서 풀이 보고 해결했다.. 간단히 loop만으로 해결되는 쉬운 문제로 보였지만, 루프마다 남은 문자 갯수를 세줘야 하는 어려운 문제이다. 

책에는 재귀함수와 스택 두가지 방법으로 풀이했지만, 스택이 더 풀이 시간도 짧고 이해하기 쉬운것 같다. (사실 원리는 두 방법 모두 동일하다.)

나중에 몇번이고 다시 풀어볼 문제이다. while문으로 조건에 따라 스택을 빼고, 그 후 넣는 스택 컨트롤 테크닉이 인상깊었다.

 + 재귀 풀이도 눈여겨 볼 법 하다. 분할 정복과 백트래킹 기법이 쓰이는데 잘 복습해야겠다.

LeetCode 739 : Daily Temperatures

문제 : https://leetcode.com/problems/daily-temperatures/submissions/

풀이 : https://daebaq27.tistory.com/40

LeetCode 42. Trapping Rain Water 문제와 풀이법이 유사하다. 같이 풀어보면 좋을 것 같다.

------------------------ 2021/10/18 ------------------

 + 개인적인 고찰 - 딕셔너리 vs 해시 테이블?
 + python 문법 - zip(), *(별표)에 대해

LeetCode 3 : Longest Substring Without Repeating Characters

문제 : https://leetcode.com/problems/longest-substring-without-repeating-characters/

풀이 : https://inspirit941.tistory.com/304 , https://codinghack.tistory.com/m/72?category=938721

해시 테이블 챕터에 있는 문제지만 투 포인터와 슬라이딩 윈도우 개념이 쓰여 어려웠다..

결국 슬라이딩 윈도우를 어케 구현할 것이냐의 문제인데, 해시 테이블(key : char, val : index)과 투 포인터를 이용해도 되지만,

직관적으로 데큐로 풀이한 것도 인상깊었다.

------------------------ 2021/10/21 ------------------

LeetCode 200 : Number of Islands

문제 : https://leetcode.com/problems/number-of-islands/

대표적인 그래프 문제라고 할 수 있다. 이 문제로 처음 DFS를 접해보았다. 뿌듯~

------------------------ 2021/10/25 ------------------

LeetCode 332 : Reconstruct Itinerary

문제 : https://leetcode.com/problems/reconstruct-itinerary/submissions/

풀이 : https://ihp001.tistory.com/98

DFS 유형의 문제이다. 다만 리프 노드부터 답에 추가하고, 리스트를 뒤집어서 답을 내는 방식을 떠올리자!

답을 보고 머릿속으로 탐색을 진행해보니까, 아니 이게 되네?

------------------------ 2021/11/01 ------------------

LeetCode 207 : Course Schedule

문제 : https://leetcode.com/problems/course-schedule/submissions/

DFS 유형 문제이나 가지치기를 통해 이미 탐색한 노드를 만날 때 백트래킹 해주는 최적화 작업이 있어야 Time Limit가 안 걸린다.

꼭 다시 풀어보자!

------------------------ 2021/11/02 ------------------

LeetCode 743 : Network Delay Time

문제 : https://leetcode.com/problems/network-delay-time/

참고 유튜브 강의 : https://www.youtube.com/watch?v=611B-9zk2o4

최단 경로 문제로, 그 중에 다익스트라 알고리즘을 이용한다.

다익스트라 첫경험이라 뭔말인지 몰라서 유튜브 찾아보고 이해했다. 유튜브 봐도 너무 어렵다.

여러번 풀어봐야 익숙해지지 않을까...

------------------------ 2021/11/03 ------------------

LeetCode 787 : Cheapest Flights Within K Stops

문제 : https://leetcode.com/problems/cheapest-flights-within-k-stops/

위에 문제랑 비슷한 유형의 최단 경로 문제이다. 위 743번과 같이 풀어보면 더 좋을 것 같다.

------------------------ 2021/11/08 ------------------

Leetcode 687 : Longest Univalue Path

문제 : https://leetcode.com/problems/longest-univalue-path/

트리 알고리즘 관련 문제이다. 2% 아쉽게 못 풀어서 여기 남겨봐요.. 한번 더 풀어보자!

------------------------ 2021/11/14 ------------------

LeetCode 297 : Serialize and Deserialize Binary Tree

문제 : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

완전 이진 트리 -> 배열 : 직렬화 , 배열 -> 완전 이진 트리 : 역직렬화 

직렬화와 역직렬화를 구현하는 문제이다. 개인적으로 배열을 문자열으로 표현하는데 있어 어려움을 겪었다.

------------------------ 2021/12/05 ------------------

LeetCode 310 : Minimum Height Trees

문제 : https://leetcode.com/problems/minimum-height-trees/

풀이 : https://devbull.xyz/leetcode-310-minimum-height-trees/

최소 높이 트리(MST) 문제이다. '최소높이트리 문제는 트리의 무게중심을 구하는 것과 같다' 를 알면 풀 수 있다!

------------------------ 2021/12/06 ------------------

LeetCode 108 : Convert Sorted Array to Binary Search Tree

문제 : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

풀이 : https://jiwon-lee-it.tistory.com/106

높이 균형(Height Balanced) 인 이진 탐색 트리(Binary Search Tree, BST) 를 만드는 문제이다.

풀이의 핵심은, 역시 트리의 기본 속성인 재귀성에 있었다.

즉, 트리의 서브트리도 모두 트리이기 때문에 재귀 형식으로 분할 정복의 풀이로 쉽게 풀리는 문제였다.

이진 탐색에서의 루틴과 같은 방법으로 HB-BST 구성이 가능하다는 점을 알게 되었다.

LeetCode 1038 : Binary Search Tree to Greater Sum Tree

문제 : https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

위 문제와 비슷한 맥락으로 풀이. 한 끗 차이라 다시 풀어보는게 좋을 듯.

------------------------ 2021/12/19 ------------------

LeetCode 336 : Palindrome Pairs

문제 : https://leetcode.com/problems/palindrome-pairs/

풀이 : https://white-board.tistory.com/131

무지성으로 브루트 포스 탐색으로는 시간초과가 나서,

시간 효율성을 위해 '트라이' 라는 자료구조를 이용해 팰린드롬 탐색을 해야 한다.

트라이 구현은 둘째 치고, 

1. 팰린드롬 조건 분기 구현 

2. 트라이 자료구조 클래스를 문제를 해결할 수 있게끔 커스텀해서 구현

이 두개가 아주아주 어려운 빡구현 문제였다. 풀이에 그래도 자세히 설명해주니까 다시 풀어보자

------------------------ 2021/12/21 ------------------

LeetCode 148 : Sort List

문제 : https://leetcode.com/problems/sort-list/

풀이 : https://daebaq27.tistory.com/34

연결 리스트 정렬을 O(nlogn) 안에 정렬해야 해서 평소 알고 있던 정렬로는 풀 수 없고,

병합 정렬 구현을 연습해볼 수 있는 문제이다. 정렬 알고리즘 연습용으로 딱 좋을 것 같다.

------------------------ 2021/12/29 ------------------

LeetCode 148 : Largest Number

문제 : https://leetcode.com/problems/largest-number/

풀이 : https://somjang.tistory.com/entry/leetCode-179-Largest-Number-Python

평범한 정렬 조건으로는 안 풀리고, 특이한 정렬 조건으로 풀어야 하는 재밌는 문제이다.

책에 있는 풀이도 좋지만, sort 함수의 key parameter를 잘 활용한 깔끔한 풀이도 같이 공유한다.

------------------------ 2022/01/04 ------------------

LeetCode 973 : K Closest Points to Origin

문제 : https://leetcode.com/problems/k-closest-points-to-origin/

투 포인터 비스무리한 풀이로 해결해볼 수 있을 것 같다.

------------------------ 2022/01/09 ------------------

LeetCode 704 : Binary Search

문제 : https://leetcode.com/problems/binary-search/

이진 검색 알고리즘을 직접 짜볼 수 있는 문제이다. 배열 인덱스 값 설정에 주의하자.

------------------------ 2022/01/18 ------------------

LeetCode 240 : Search a 2D Matrix II

문제 : https://leetcode.com/problems/search-a-2d-matrix-ii/

풀이 : https://velog.io/@pyh8618/LeetCode-240.-Search-a-2D-Matrix-II

이진 검색을 이용해서 복잡하게 풀어야 할 것 같지만 풀이는 창의적으로 간단하게 해결했더라.

다시 풀면 이런 풀이가 있었지, 하고 넘기면 될 것 같다. (그냥 알고리즘을 고민하면 되는 문제!)

------------------------ 2022/02/13 ------------------

LeetCode 76 : Minimum Window Substring

문제 : https://leetcode.com/problems/minimum-window-substring/

풀이 : https://ihp001.tistory.com/116

슬라이딩 윈도우(투 포인터) 풀이로 해결이 가능하다. 문제 해결 접근은 비슷하게 잘 접근했으나

변수 설정과 해결 조건을 정교하게 설계하지 못한 것 같아 아쉽다. 좋은 문제이니 다시 풀어볼 것.

------------------------ 2022/02/27 ------------------

LeetCode 406 : Queue Reconstruction by Height

문제 : https://leetcode.com/problems/queue-reconstruction-by-height/

풀이 : https://8iggy.tistory.com/138

그리디 알고리즘을 연습해볼 수 있는 문제이다. 그리디 알고리즘은 데이터가 들어올때마다 그때그때 최적해를 찾을 수 있도록 하는 것이다.

다시 말해, 루프 중간에 빠져나와도 그 결과값은 루프 중간까지의 정답이 들어가 있어야 한다.



LeetCode 621 : Task Scheduler

문제 : https://leetcode.com/problems/task-scheduler/

풀이 : https://withhamit.tistory.com/419

이것도 그리디 알고리즘 문제이다. 책의 풀이가 복잡해서 인터넷에 있는 고수의 풀이를 참고해서 풀었다.

느낀 점은 이 고수처럼 나도 풀 때 손으로 끄적이면서 먼저 풀어보는 게 아주 중요한 것 같다.

역시 잘하는 사람은 뭔가 다른 게 있나보다. 고수의 풀이가 감명깊었다.

------------------------ 2022/03/07 ------------------

LeetCode 169 : Majority Element

문제 : https://leetcode.com/problems/majority-element/

분할 정복(Divide and Conquer) 알고리즘 맛보기 유형..

------------------------------------------------------------------------------------------

위에까지는 '파이썬 알고리즘 인터뷰' 책의 문제를 풀이해봤고,

이제부터는 백준 알고리즘 문제를 풀어볼 생각이다.


※ 그리디 알고리즘 ※

------------------------ 2022/03/13 ------------------

백준 1931 : 회의실 배정 (S2)

문제 : https://www.acmicpc.net/problem/1931

풀이 : https://suri78.tistory.com/26

대충 알고리즘 문제를 풀다 막혔을 때 아래와 같은 절차로 해결해나가면 된다.

문제풀이 알고리즘 떠올리기(알고리즘 공부!!) -> 효율성 찾기(다른 알고리즘 or 자료구조 적용) -> 엣지케이스 찾기

이번에는 문제해결 아이디어도 잘 떠올렸지만, 문제를 잘 읽어봤을때 핵심이 되는 케이스를 간과해서 엣지케이스를 못 찾아서 실패한 경우이다.

+ 그리디 알고리즘은 쉽게 답이 나온다. 코드 설계 단계에서 복잡하게 생각하지 말 것.

2차 풀이(O) - 2022/03/28 

------------------------ 2022/03/27 ------------------

백준 1202 : 보석 도둑 (G2)

문제 : https://www.acmicpc.net/problem/1202

풀이 : https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-1202-%EB%B3%B4%EC%84%9D-%EB%8F%84%EB%91%91-Python

두가지 변인이 존재하고 한가지 변인의 조건이 주어지고, 그 조건을 만족하는 새 그룹 안에서 나머지 변인의 최대 or 최소를 구하는 문제이다.

처음에는 한 변인의 조건을 바탕으로 슬라이싱을 통해 재그룹하고, 그 슬라이스 내에서 max를 이용한 최댓값을 구하려고 했으나 --> 시간 초과

올바른 접근 방법 : 최소힙, 최대힙을 이용하는 것.


※ 그래프 이론 () ※

------------------------ 2022/04/07 ------------------

백준 2178 : 미로 탐색 (S1)

문제 : https://www.acmicpc.net/problem/2178

풀이 : https://yongku.tistory.com/1956

DFS로 풀었는데, 풀이가 잘 떠오르지 않았다.

최단 경로를 풀 때는 BFS로 풀어야겠다. 

아직 많이 부족한 것 같다. 풀이를 보고 그래프 문제 구현 테크닉을 먼저 익혀야겠다.

2차 풀이(△) - 2022/05/11 - 풀이를 참고했다. BFS 구현 테크닉을 익힐 수 있었다.

------------------------ 2022/05/13 ------------------

★DFS 풀이 꿀팁★

파이썬의 재귀 깊이 제한은 1000정도로 얕은 편이다. 만약에 RecursionError가 발생할 경우,

sys.setrecursionlimit(10 ** 6) <-- 이 코드를 통해 재귀 깊이를 깊게 잡아야 한다. 매우 꿀팁

------------------------ 2022/05/14 ------------------

백준 7576 : 토마토 (G5)

문제 : https://www.acmicpc.net/problem/7576

풀이 : https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8

BFS에서 그 이전 결과값에 따른 변수를 배열에 저장하는 테크닉 (<-- 해 보면 알것이다) 땜에 시간초과로 아쉽게 못 품..

------------------------ 2022/05/16 ------------------

오늘의 팁 .. python으로 시간초과 뜰 때 pypy3으로 제출해볼 것.

(알고리즘을 개선해서 시간초과를 해결해볼 수도 있지만, 그래도 푼게 아까우니까)

문제 - 백준 14502 연구소 : https://www.acmicpc.net/problem/14502
