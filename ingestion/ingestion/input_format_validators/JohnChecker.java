import java.util.*;

// Checker for Question of Ingestion

public class JohnChecker
{
    public static final int MINN = 1;
	public static final int MAXN = 100;
    public static final int MINM = 1;
	public static final int MAXM = 20000;

	public static String [] lines = new String[MAXM];

	public static void printError(int line, String msg)
	{
		System.out.println("ERROR Line " + line + ": " + msg);
		System.exit(-1);
	}

    public static void checkIntBounds(int x, int min, int max, String name, int nLines)
    {
        if (x < min || x > max)
            printError(nLines, "invalid " + name + " value: " + x);
    }

    public static void checkForRepeats(int size, int nLines)
    {
        for(int i=0; i<size-1; i++)
            if (lines[i].equals(lines[size-1]))
                printError(nLines, "repeated line " + lines[size-1]);
    }
	public static void main(String [] args)
	{
		Scanner in = new Scanner(System.in);
		int n, m, nLines = 0;
		String line;

        line = in.nextLine();
        nLines++;
        StringTokenizer st = new StringTokenizer(line);
        if (st.countTokens() != 2)
            printError(nLines, "number of values on line incorrect");
		n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
		checkIntBounds(n, MINM, MAXM, "n", nLines);
		checkIntBounds(m, MINM, MAXM, "m", nLines);
		while (in.hasNext()) {
			line = in.nextLine();
			nLines++;
			st = new StringTokenizer(line);
			if (st.countTokens() != n) {
                printError(nLines, "number of values on line incorrect");
                continue;
			}
			for(int i=0; i<n; i++) {
                int val = Integer.parseInt(st.nextToken());
                checkIntBounds(val, 1, 1000000, "course calories", nLines);
			}
		}
		if (in.hasNextLine())
			printError(nLines, "extra number of lines");
System.exit(42);
	}
}

