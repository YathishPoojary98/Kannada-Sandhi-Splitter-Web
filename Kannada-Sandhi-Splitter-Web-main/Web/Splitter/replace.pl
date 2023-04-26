open(INFILE,"<output.txt") or die "Could not read the file $!\n";
@lines = <INFILE>;
close INFILE;
open(OUTFILE,">finalout.txt") or die "Could not write to the file $!\n";
foreach $line (@lines)
{
$line=~s/ಜಸ್ತ್ವ/ಜಶ್ತ್ವ/;
print OUTFILE $line;
}
