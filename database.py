from backend import Employee
import os

def legacyCSV(empDict = None) -> dict: 
    """
    Calls in a legacy database CSV and saves it to whatever the default type is. Takes no parameters and returns a dictionary. 
    Will call for a dialog box 

    Returns
    -------
    A dictionary of Employees where the key is the Employee ID to the corresponding value

    See Also
    --------
    TODO
    """
    #TODO   Open Dialog box to get legacy code location

    f = open('legacy/employees.csv','r').readlines()[1:]
    empDict = {}

    #TODO   multiprocess here
    #Grabs all relevant parts
    for line in f:
        line = line.split(',')
        empID = int(line[0])
        empName =       line[1]
        empStreet =     line[2]
        empCity =       line[3]
        empState =      line[4]
        empZip =        line[5]
        empClass =      line[6]
        empPay =        line[7]
        # empSalary =     line[8]     #vvvvv To be used once Employee is fleshed out vvvvv
        # empHourly =     line[9]
        # empCommision =  line[10]
        # empRoute =      line[11]
        # empAccount =    line[12]

        #Using old Employee object
        empDict[empID] = Employee(empID, empName, empStreet, empCity, empState, empZip, empClass, empPay)
    
    #TODO transalate to new database
    #TODO record new database location

    return empDict
def importDatabase(file = None, cfg = None) -> dict:
    """
    `importDatabase` creates and returns a dictionary of all valid employee objects that are able to be loaded from memory.
    This function takes in two parameters, neither of which are required for this to function. Both parameters act as an override
    to base functionallity. This function should be ran at startup. This function calls importCSV and getConfig

    Parameters
    ----------
    file : str or lyst
        `file` is the file location of the database that should be loaded, default location is stored in the config.cfg
    config : dict
        A dictionary carrying specific values to how our data is formatted. Values called here are 'preferedFormat' and 'dataToPull'

    Returns
    -------
    A dictionary of Employees where the key is the Employee ID to the corresponding value
    """
    if cfg == None:
        cfg = getConfig(1)
    if file == None:
        file = cfg['dataToPull']

    if cfg['preferedFormat'] == 'csv':
        return importCSV(file)
    elif cfg['preferedFormat'] == 'xml':
        return importXML(file)
    elif cfg['preferedFormat'] == 'json':
        return importJSON(file)
    else:
        raise SyntaxError(cfg['preferedFormat'], 'Error in Config')
def importCSV(fileName: str) -> dict:
    """
    To be used by importDatabase if prefered filetype is CSV, not to be called piecewise

    Paramaters
    ----------
    filename : str
        The location of the database provided to the function

    Returns
    -------
    Returns a dictionary filled with employee objects from backend.py
    """
        #TODO   Open Dialog box to get legacy code location

    f = open(fileName).readlines()[1:]
    empDict = {}

    #TODO   multiprocess here
    for line in f:
        line = line.split(',')
        empID = int(line[0])
        empName =       line[1]
        empStreet =     line[2]
        empCity =       line[3]
        empState =      line[4]
        empZip =        line[5]
        empClass =      line[6]
        empPay =        line[7]
        # empSalary =     line[8]     #vvvvv To be used once Employee is fleshed out vvvvv
        # empHourly =     line[9]
        # empCommision =  line[10]
        # empRoute =      line[11]
        # empAccount =    line[12]

        #Using old Employee object
        empDict[empID] = Employee(empID, empName, empStreet, empCity, empState, empZip, empClass, empPay)
    
    #TODO transalate to new database
    #TODO record new database location

    return empDict
def importXML(fileName: str) -> dict:
    """
    To be used by importDatabase if prefered filetype is XML, not to be called piecewise

    Paramaters
    ----------
    filename : str
        The location of the database provided to the function

    Returns
    -------
    Returns a dictionary filled with employee objects from backend.py
    """
    #TODO
    raise NotImplementedError()
def importJSON(fileName: str) -> dict:
    """
    To be used by importDatabase if prefered filetype is JSON, not to be called piecewise

    Paramaters
    ----------
    filename : str
        The location of the database provided to the function

    Returns
    -------
    Returns a dictionary filled with employee objects from backend.py
    """
    #TODO
    raise NotImplementedError()

def removeEmployee(empID: int, user: int, reason: str or list, file = None) -> None:
    """
    Puts the employee into a queue to be changed upon the request of an admin. Removed employee is stored in a local file
    until such time that it can be approved. This function works in conjunction with approveRemove and may depend upon
    getConfig if no file parameter is supplied as a manual overide.

    Parameters
    ----------
    empID : int
        Employee ID of the person being removed.
    user : int
        Employee ID of the person requesting the removal.
    reason : str or list
        The string documenting the reason for removal, or a list containing strings of reasons submitted to be recorded in the system.
    file : str
        A manual overide to provide with the dat file where removal requests are stored.
    """
    if file == None:
        file = getConfig(1)['changeRequest']

    #get last ticket number
    ticketNumber = 0
    if os.stat(file).st_size != 0:                          #check for empty file
        with open(file) as f:
            ticketNumber = int(f.readlines()[-1].split(' - ')[0]) + 1
    
    #TODO implement list for reason
    #TODO check for duplicate submissions

    with open(file,'a') as f:
        f.write(f'{ticketNumber} - Requested:{user} - Employee:{empID} - Reason:{reason}\n')

    #####################################################################################################
    #     lastLine = ''
    #     with open(file, 'rb') as f:                         #seek from the end while reading in binary
    #         f.seek(-2, os.SEEK_END)
    #         while f.read(1) != b'\n':                       #search for newline
    #             f.seek(-2, os.SEEK_CUR)
    #         lastLine = f.readline().decode()
    #     ticketNumber = int(lastLine.split(' - ')[0]) + 1    #set to last ticketNumber
    #####################################################################################################
def approveRemove(ticket: int or list, user: int, empDict: dict, pull=None, push=None) -> dict:
    """
    Removes ticket from the file, and the corresponding employee from the database when proper information is provided.
    Employee is archived into the appropriate file, and a new dictionary is returned with the nessasecry modifications
    made to it.

    This function works in concert with removeEmployee and may depend on getConfig if the appropirate overrides are
    not given

    Parameters
    ----------
    ticket : int or list
        Takes either a single int representing a ticket based on queue file, or a list of tickets to be removed.
    user : int
        The approving admin for removal, cannot be the same admin that requested the change
    empDict : dict
        The employee database object
    pull : str
        An override to the base path for our queue. This does not need to be filled and can be pulled from using
        getConfig.
    puss : str
        An override to the base path for our archive. This does not need to be filled and can be pulled from using
        getConfig.

    Returns
    -------
    Returns an updated dictionary with the appropriate changes made
    """
    # if pull == None or push == None:
    #     cfg = getConfig(1)
    #     pull = cfg['changeRequest']
    #     push = cfg['employeeArchive']
    
    # issues = {}
    # with open(pull) as f:
    #     archive = f.readlines().split(' - ')
    #     for item in archive:
    #         issues[item[0]] = item[1:].append(empDict[empID])

    raise NotImplementedError()
def writeEmployee(empID: int, user: int, reason: str or list, file = None) -> None:
    """
    Puts the employee into a queue to be changed upon the request of an admin or the employee. Removed employee is 
    stored in a local file until such time that it can be approved. This function works in conjunction with approveWrite 
    and may depend upon getConfig if no file parameter is supplied as a manual overide.

    Parameters
    ----------
    empID : int
        Employee ID of the person being removed.
    user : int
        Employee ID of the person requesting the removal.
    reason : str or list
        The string documenting the reason for removal, or a list containing strings of reasons submitted to be recorded in the system.
    file : str
        A manual overide to provide with the dat file where removal requests are stored.
    """
    raise NotImplementedError()
def approveWrite(ticket: int or list, user: int, empDict: dict, pull=None, push=None) -> dict:
    """
    Removes ticket from the file, and applies changes to the corresponding employee in the database when proper information is provided.
    Employee is changed in the appropriate file, and a new dictionary is returned with the nessasecry modifications made to it.

    This function works in concert with removeEmployee and may depend on getConfig if the appropirate overrides are
    not given

    Parameters
    ----------
    ticket : int or list
        Takes either a single int representing a ticket based on queue file, or a list of tickets to be approved.
    user : int
        The approving admin for the change
    empDict : dict
        The employee database object
    pull : str
        An override to the base path for our queue. This does not need to be filled and can be pulled from using
        getConfig.
    puss : str
        An override to the base path for our archive. This does not need to be filled and can be pulled from using
        getConfig.

    Returns
    -------
    Returns an updated dictionary with the appropriate changes made
    """
    raise NotImplementedError()

def getConfig(index : int or list, cfgFile = "config.cfg") -> dict:
    """
    Gets parameters from config file saved to an accessible directory

    Parameters
    ----------
    cfgFile : str
        file location of cfg, defaults to current location
    index : int or list
        the index or indeces that are needed from config, in general
        1: File Information
        
        With other lines to be assigned as needed.
    
    Returns
    -------
    A dictionary with information on saves, user prefs, etc.

    See Also
    --------
    TODO
    """
    cfg = {}
    #Get single line of the config
    if type(index) == int:
        f = open(cfgFile).readlines()[index - 1].split(',')
        for cell in f:
            cell = cell.split('=')
            cfg[cell[0]] = cell[1][1:-1]
    #Get multiple lines of the config
    elif type(index) == list and type(index[0]) == int:
        f = open(cfgFile).readlines()
        j = []
        for i in index:
            j.append(f[i - 1])
        for cell in j:
            cell = cell.split('=')
            cfg[cell[0]] = cell[1][1:-1]
    else:
        raise SyntaxError(index, 'Must be either an int or list')
    return cfg

if __name__ == '__main__':
    legacyCSV()
    importDatabase()
    removeEmployee(123125,123123,'asdf')
    removeEmployee(123124,123123,'asdf')