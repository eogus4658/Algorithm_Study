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
