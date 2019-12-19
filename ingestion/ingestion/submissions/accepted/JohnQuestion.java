import java.util.*;

public class JohnQuestion
{
    public static final int MAXINTAKE = 20000;
    public static final int MAXROWS = 25;	    	// number of times 20000 can be divided by 1.5
    public static final int MAXCOLS = 1000;		// number of courses

    public static Scanner in = new Scanner(System.in);

    public static cell [][] table = new cell[MAXROWS][MAXCOLS+3];

    public static int [] courses = new int[MAXCOLS+3];			// three dummy courses to start
    public static int [] intake;

    public static void buildTable(int nrows, int ncols)
    {
        for(int r=0; r<nrows; r++)
            for(int c=0; c<ncols; c++)
                table[r][c] = new cell();
        for(int c=0; c<3; c++)				// init table
            for(int r=0; r<nrows; r++)
                table[r][c].val = 0;
        for(int c=3; c<ncols; c++)
            table[0][c].val = 0;				// stores maximum in each row
        for(int c=3; c<ncols; c++) {
            for(int r=1; r<nrows-1; r++) {
                table[r][c].val = Math.min(courses[c], intake[r]);
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
            table[nrows-1][c].val = Math.min(courses[c], intake[nrows-1]);
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

    public static void main(String [] args)
    {
        int n, maxintake;
        n = in.nextInt();
        maxintake = in.nextInt();
        courses[0] = courses[1] = courses[2] = 0;
        for(int i=0; i<n; i++)
            courses[i+3] = in.nextInt();
        int nrows = (int)(Math.log(maxintake)/Math.log(1.5) + 1);    // # times maxintake can be divided by 1.5
        intake = new int[nrows];
        intake[nrows-1] = maxintake;
        for(int i=nrows-2; i>=0; i--) {
            intake[i] = (int)(intake[i+1]/1.5);
        }
        buildTable(nrows, n+3);
        System.out.println(table[0][n+2].val);
    }
}

class cell
{
	public int val;
	public int prevc, prevr;
}

