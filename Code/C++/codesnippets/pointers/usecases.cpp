

// pass pointer
void bypointer(yourClassName* instanceName)
{
	//changes the object that is OUTSIDE the function!
	instanceName->classVariable += 1;

	//instanceName->classVariable = instanceName->classVariable + 1; //same as above
	//(*instanceName)++;//actually changes the yourClassName
	//Danger! instanceName++;//changes the memory address location
	//Danger! instanceName = instanceName + 1000;//changes the memory address location	
}

yourClassName byValue(yourClassName instanceName)//trigger a copy event
{
	//will make a copy of instanceName!
	//changes the object that is INSIDE the function!
	instanceName.classVariable += 10;
	return instanceName;
}

void byRefenceAddress(yourClassName &instanceName)
{
	//will make a copy of instanceName!
	//changes the object that is OUTSIDE the function!
	instanceName.classVariable += 100;
}

yourClassName constReference(const yourClassName &instanceName)
{
	//will make a copy of instanceName!
	//we cannot modify it
	//not possible t.classVariable += 0.1;
	yourClassName instanceName_new;
	instanceName_new = instanceName.classVariable + 1000;
	return instanceName_new;
}



void main(){

    yourClassName instanceName(20);//Calling the constructor - we have created an "instance" of the "object"

	yourClassName* pointerToInstance(0);//Calling the constructor
	yourClassName* pO(nullptr);

	pointerToInstance = &instanceName;
	pO = &tO;

	//try ....
	yourClassName* pAverage = new yourClassName();

		std::cerr << "\nInitial yourClassName: " << instanceName.classVariable;
		yourClassName(pointerToInstance);
		std::cerr << "\n By Pointer";
		std::cerr << "\nInitial yourClassName: " << instanceName.classVariable ;
        std::cerr <<  " instanceName(pointer): " << pointerToInstance->classVariable;

		yourClassName returnedT = byValue(instanceName);
		std::cerr << "\n By Value";
		std::cerr << "\nInitial yourClassName: " << instanceName.classVariable << " instanceName(pointer): " << pointerToInstance->classVariable << " returned: " << returnedT.classVariable;

		//void byRefenceAddress(yourClassName& t) -- add 100 - Safe ! Does allow editing (but does not allow to change the actual pointer)
		byRefenceAddress(instanceName);
		
		//yourClassName increaseclassVariablePassByReference3_Const(const yourClassName & t) - Safe and does not allow editing
		yourClassName returnedConstant = constReference(instanceName);
	
	
	}
}