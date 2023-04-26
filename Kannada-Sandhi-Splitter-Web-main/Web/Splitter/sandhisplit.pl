open(INFILE,"<inputwords.txt") or die "Could not open the file $!\n";
open(F1, ">", 'correctoutputs.txt');
open(F2, ">", 'erroroutputs.txt');
@wordlist = <INFILE>;
foreach $word (@wordlist)
{
chomp($word);
$res = `python utf2wx.py $word`;
chomp($res);
print "$res\n";
$res1 = `python correct_sandhi_mod.py $res`;
print "$res1";
}
close INFILE,F1,F2;
