#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const int MAXINTAKE = 20000;
const int MAXROWS = 25;	    	// number of times 20000 can be divided by 1.5
const int MAXCOLS = 1000;		// number of courses

class cell
{
public:
	int val;
	int prevc, prevr;
} table[MAXROWS][MAXCOLS+3];

int courses[MAXCOLS+3];			// three dummy courses to start
int *intake;

void printTable(int nrows, int ncols)
{
	for(int r=nrows-1; r>=0; r--) {
		for(int c=0; c<ncols; c++)
			printf("%5d", table[r][c].val);
		cout << endl;
	}
}

void printCals(int r, int c)
{
	if (c >= 3) {
		printCals(table[r][c].prevr, table[r][c].prevc);
		if (table[r][c].prevc < 3) {
			for(int i=2; i<c-1; i++)
				cout << 0 << ' ';
		}
		else {
			for(int i=table[r][c].prevc; i<c-1; i++)
				cout << 0 << ' ';
		}
		cout << table[r][c].val << ' ';
	}
}

void buildTable(int nrows, int ncols)
{
	for(int c=0; c<3; c++)				// init table
		for(int r=0; r<nrows; r++)
			table[r][c].val = 0;
	for(int c=3; c<ncols; c++)
		table[0][c].val = 0;				// stores maximum in each row
	for(int c=3; c<ncols; c++) {
		for(int r=1; r<nrows-1; r++) {
			table[r][c].val = min(courses[c], intake[r]);
			if (table[r+1][c-1].val > table[r][c-2].val) {
				table[r][c].val += table[r+1][c-1].val;
				table[r][c].prevc = c-1;
				table[r][c].prevr = r+1;
			}
			else {
				table[r][c].val += table[r][c-2].val;
				table[r][c].prevc = c-2;
				table[r][c].prevr = r;
			}
			if (table[r][c].val > table[0][c].val) {
				table[0][c].val = table[r][c].val;
				table[0][c].prevr = r;
			}
		}
		table[nrows-1][c].val = min(courses[c], intake[nrows-1]);
		if (table[nrows-1][c-2].val > table[0][c-3].val) {
			table[nrows-1][c].val += table[nrows-1][c-2].val;
			table[nrows-1][c].prevc = c-2;
			table[nrows-1][c].prevr = nrows-1;
		}
		else {
			table[nrows-1][c].val += table[0][c-3].val;
			table[nrows-1][c].prevc = c-3;
			table[nrows-1][c].prevr = table[0][c-3].prevr;
		}
		if (table[nrows-1][c].val > table[0][c].val) {
			table[0][c].val = table[nrows-1][c].val;
			table[0][c].prevr = nrows-1;
		}
	}
}

int main()
{
	int n, maxintake;
	cin >> n;
	cin >> maxintake;
	courses[0] = courses[1] = courses[2] = 0;
	for(int i=0; i<n; i++)
		cin >> courses[i+3];
    int nrows = log(maxintake)/log(1.5) + 1;    // # times maxintake can be divided by 1.5
    intake = new int[nrows];
	intake[nrows-1] = maxintake;
	for(int i=nrows-2; i>=0; i--) {
		intake[i] = intake[i+1]/1.5;
	}
	buildTable(nrows, n+3);
	cout << table[0][n+2].val << endl;
//	printCals(table[0][n+2].prevr, n+2);
//	cout << endl;
//	printTable(MAXROWS, n+3);
}


