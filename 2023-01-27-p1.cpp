// Leaders
// http://usaco.org/index.php?page=viewproblem&cpid=1263

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// a leader:
    // must include all cows of their breed, or
    // include other breed's leader
// the problem must have at least one ownBreedLeader

int main() {
    int cowCount = 0;
    string cowTypes;
    cin >> cowCount >> cowTypes;

    vector<int> ranges(cowCount);
    for (int i = 0; i < cowCount; i++) {
        cin >> ranges[i];
        ranges[i]--;
    }

    // find the index of left and right most G's and H's
    int leftH = cowTypes.find_first_of('H');
    int leftG = cowTypes.find_first_of('G');
    int rightH = cowTypes.find_last_of('H');
    int rightG = cowTypes.find_last_of('G');

    // check if we have two own-breed leaders
    bool twoOwnLeaders = (leftG < leftH && ranges[0] >= rightG) || (leftG > leftH && ranges[0] >= rightH);

    // count how many leaders on the left of the right-most cow leader
    // note a leader can either a) include all cows of their breed, or b) include the right-most cow leader
    int answer = 0;
    for (int i = 0; i < max(leftG, leftH); i++) {
        if ((i == 0 && twoOwnLeaders) || (ranges[i] >= max(leftG, leftH))) {
            answer++;
        }
    }

    cout << answer << endl;
    return 0;
}
