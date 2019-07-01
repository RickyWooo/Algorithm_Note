first of all, my solution was like 

1. Import an ASCII CHAR as an set
2. Check each char in the string if in the set or not
3. If the char appear over once, return False

But there should be a more simpler solution

1. Check the length of the string, if > 128 return false(assume ASCII not Unicode)
2. Declare a set with length 128
3. Iterative the string and get value from the index, set the appear char as true
4. if the char is true, then return false indicated it came up before

```java
public static boolean isUniqueChars(String str) {
		if (str.length() > 128) {
			return false;
		}
		boolean[] char_set = new boolean[128];
		for (int i = 0; i < str.length(); i++) {
			int val = str.charAt(i);
			if (char_set[val]) return false;
			char_set[val] = true;
		}
		return true;
	}
```