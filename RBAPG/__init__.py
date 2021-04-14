"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || |   ______     | || |      __      | || |   ______     | || |    ______    | |
| | |_   __ \    | || |  |_   _ \    | || |     /  \     | || |  |_   __ \   | || |  .' ___  |   | |
| |   | |__) |   | || |    | |_) |   | || |    / /\ \    | || |    | |__) |  | || | / .'   \_|   | |
| |   |  __ /    | || |    |  __'.   | || |   / ____ \   | || |    |  ___/   | || | | |    ____  | |
| |  _| |  \ \_  | || |   _| |__) |  | || | _/ /    \ \_ | || |   _| |_      | || | \ `.___]  _| | |
| | |____| |___| | || |  |_______/   | || ||____|  |____|| || |  |_____|     | || |  `._____.'   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
						BY:Aziz Kaplan
						Github:https://www.github.com/AzizKpln
						Youtube:https://www.youtube.com/channel/UCHGEA5g4iFDdBognYNWCJbA
						Note:Do not use it in illegal projects ;)

[!]To get help about usage, read the README.MD on github
https://www.github.com/AzizKpln/RBAPG
"""
import logging
import sys
import itertools
class RuleBasedAttackPasswordGenerator:
	def __init__(self):
		self._wordlist="You haven't specified a wordlist"
		self.repeating_off=set()
		self._repeating_off=set()
		self._situation=False
		self.length_of_wordlist=None
		self._wordlistName="wordlist.txt"
		self._length_of_password=None
		self._repeat_counter=0
		self.repeat_counter=0
		self.Combine=0
		self.enhancer=0
		self.logging_module_errors()
	def __help__(self):
		print("https://github.com/AzizKpln/RBAPG")
	def logging_module_errors(self):
		logging.basicConfig(level=logging.DEBUG)
	@property
	def wordlist(self):
		return self._wordlist
	@wordlist.setter
	def wordlist(self,val):
		self._wordlist=val
	@property
	def save(self):
		return self._situation
	@save.setter
	def save(self,val=True):
		self._situation=val
	def getWordlistName(self):
		return self._wordlistName
	def setWordlistName(self,val):
		self._wordlistName=val
	def getLengthOfGeneratedPassword(self):
		return self._length_of_password
	def setLengthOfGeneratedPassword(self,val):
		if val>5:
			logging.getLogger().error(f"This feature takes value 'maximum 5' but you specified '{val}' !!",stack_info=True)
			sys.exit()
		elif val<2:
			logging.getLogger().error(f"This feature takes value 'minimum 2' but you specified '{val}' !!",stack_info=True)
			sys.exit()
		else:
			self._length_of_password=val
	def for_loop(self,generate_wordlist_=None,var=None,var1=None,var2=None,var3=None):
		if self._length_of_password==2:
			self.length_of_password2=(generate_wordlist_[self.enhancer]+generate_wordlist_[var])
			self.repeating_off.add(self.length_of_password2)
		if self._length_of_password==3:
			self.lop_a=(generate_wordlist_[self.enhancer]+generate_wordlist_[var1])
			self.length_of_password2=(generate_wordlist_[self.enhancer]+generate_wordlist_[var])
			self.length_of_password3=(generate_wordlist_[self.enhancer]+generate_wordlist_[var]+generate_wordlist_[var1])
			self.repeating_off.add(self.length_of_password2)
			self.repeating_off.add(self.lop_a)
			self.repeating_off.add(self.length_of_password3)
		if self._length_of_password==4:
			self.lop_a=(generate_wordlist_[self.enhancer]+generate_wordlist_[var1])
			self.shuffle=(generate_wordlist_[self.enhancer]+generate_wordlist_[var2])
			self.length_of_password2=(generate_wordlist_[self.enhancer]+generate_wordlist_[var])
			self.length_of_password3=(generate_wordlist_[self.enhancer]+generate_wordlist_[var]+generate_wordlist_[var1])
			self.length_of_password4=(generate_wordlist_[self.enhancer]+generate_wordlist_[var]+generate_wordlist_[var1]+generate_wordlist_[var2])
			self.repeating_off.add(self.length_of_password2)
			self.repeating_off.add(self.lop_a)
			self.repeating_off.add(self.shuffle)
			self.repeating_off.add(self.length_of_password3)
			self.repeating_off.add(self.length_of_password4)
		if self._length_of_password==5:
			self.lop_a=(generate_wordlist_[self.enhancer]+generate_wordlist_[var1])
			self.shuffle=(generate_wordlist_[self.enhancer]+generate_wordlist_[var2])
			self.shuffleX=(generate_wordlist_[self.enhancer]+generate_wordlist_[var3])
			self.length_of_password2=(generate_wordlist_[self.enhancer]+generate_wordlist_[var])
			self.length_of_password3=(generate_wordlist_[self.enhancer]+generate_wordlist_[var]+generate_wordlist_[var1])
			self.length_of_password4=(generate_wordlist_[self.enhancer]+generate_wordlist_[var]+generate_wordlist_[var1]+generate_wordlist_[var2])
			self.length_of_password5=(generate_wordlist_[self.enhancer]+generate_wordlist_[var]+generate_wordlist_[var1]+generate_wordlist_[var2]+generate_wordlist_[var3])
			self.repeating_off.add(self.length_of_password2)
			self.repeating_off.add(self.lop_a)
			self.repeating_off.add(self.shuffle)
			self.repeating_off.add(self.length_of_password3)
			self.repeating_off.add(self.length_of_password4)
			self.repeating_off.add(self.shuffleX)

	def loop_for_combination(self,length_,generate_wordlist_):
		while(self.enhancer<length_):
			if(self._length_of_password==2):
				for i in range(0,length_):
					self.for_loop(generate_wordlist_,i)
			if(self._length_of_password==3):
				for i in range(0,length_):
					for q in range(0,length_):
						self.for_loop(generate_wordlist_,i,q)
			if(self._length_of_password==4):
				for i in range(0,length_):
					for q in range(0,length_):
						for j in range(0,length_):
							self.for_loop(generate_wordlist_,i,q,j)
			if(self._length_of_password==5):
				for i in range(0,length_):
					for q in range(0,length_):
						for j in range(0,length_):
							for degiskenkalmadiabi in range(0,length_):
								self.for_loop(generate_wordlist_,i,q,j,degiskenkalmadiabi)
			self.enhancer+=1
	def SplitWordlist(self):
		generate_wordlist_=self._wordlist.split(" ")
		self.loop_for_combination(len(generate_wordlist_),generate_wordlist_)



	####OPTIONAL_FUNCTION####
	def CombineTheWords(self):
		####NOT RECOMMENDED FOR HUDE CONTENT OF WORDLIST####
		self.SplitWordlist()
		for combine in self.repeating_off:
			for combine_iter in itertools.permutations(combine):
				with open(self._wordlistName,"a+",encoding="utf-8") as _write:
					_write.write(''.join(combine_iter)+"\n")
				print(''.join(combine_iter))
	####OPTIONAL_FUNCTION####
	def CombineCozily(self):
		self.SplitWordlist()
		self.repeating_off=list(self.repeating_off)
		while(self._repeat_counter<int(len(self.repeating_off))):
			self.repeat_counter=0
			while(self.repeat_counter<(int(float(len(self.repeating_off[self._repeat_counter])))-4)):
				self.CombineCozilyAdd()
				for j in range(1,5):
					val=str(self.repeating_off[self._repeat_counter][self.repeat_counter:j])
					val1=str(self.repeating_off[self._repeat_counter][j:j+(j*4)])
					val2=str(self.repeating_off[self._repeat_counter][j:])
					val3=str(self.repeating_off[self._repeat_counter][j::2])
					if not int(len(val))<4:
						self._repeating_off.add(val)
					if not int(len(val1))<4:
						self._repeating_off.add(val1)
					if not int(len(val2))<4:
						self._repeating_off.add(val2)
					if not int(len(val3))<4:
						self._repeating_off.add(val3)
				self.repeat_counter+=1
			self._repeat_counter+=1
		self.CombineCozilyPrint()
		self.CombineCozilySave()
	def CombineCozilyAdd(self):
		val=str(self.repeating_off[self._repeat_counter][self.repeat_counter::])
		self._repeating_off.add(val)
	def CombineCozilyPrint(self):
		for i in self._repeating_off:
			print(i)
	def CombineCozilySave(self):
		for cozy_save in self._repeating_off:
			with open(self._wordlistName,"a+",encoding="utf-8") as _write:
				_write.write(cozy_save+"\n")
	def wordlistSave(self):
		for wr in self.repeating_off:
			with open(self._wordlistName,"a+",encoding="utf-8") as _write:
				_write.write(wr+"\n")
			print(wr)
	def generate_wordlist(self):
		if self._length_of_password==None:
			logging.getLogger().error(f"You Have To Specify The Function:setLengthOfGeneratedPassword(min2-max5) !!",stack_info=True)
			sys.exit()
		generate_wordlist_=self._wordlist.split(" ")
		self.loop_for_combination(len(generate_wordlist_),generate_wordlist_)
		self.wordlistSave()

	LengthOfGeneratedPassword=property(getLengthOfGeneratedPassword,setLengthOfGeneratedPassword)
	WordlistName=property(getWordlistName,setWordlistName)
