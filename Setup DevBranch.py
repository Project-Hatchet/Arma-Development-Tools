
import winreg

class GetRegistryValues():
    """Class to get all the paths of the registry keys.

    Args:
        hkey (Const): any one of the predefined HKEY_* constants]
            {HKEY_CLASSES_ROOT,
            HKEY_CURRENT_USER,
            HKEY_LOCAL_MACHINE,
            HKEY_USERS,
            HKEY_CURRENT_CONFIG}

        sub_key (str): the subkey to open
        value_name (str): the value to retrieve
    """
    def __init__(self, hkey = -1, sub_key = -1, value_name = -1):
        self._hkey = hkey
        self._sub_key = sub_key
        self._value_name = value_name

    def get_value_name(self):
        return self._value_name

    def set_value_name(self, value):
        self._value_name = value

    def set_sub_key(self, sub_key):
        self._sub_key = sub_key

    def set_hkey_const(self, hkey):
        pass

    def __str__(self):
        return f'{self.value_name}'

    def get_hkey_const(self, hkey):
        """Return the root key for the given root key name.

        Args:
            hkey (str): the name of the root key

        Returns:
            Const: one of the predefined HKEY_* constants]
        """
        # Get the root key
        if hkey == "HKEY_CLASSES_ROOT":
            return winreg.HKEY_CLASSES_ROOT
        elif hkey == "HKEY_CURRENT_USER":
            return winreg.HKEY_CURRENT_USER
        elif hkey == "HKEY_LOCAL_MACHINE":
            return winreg.HKEY_LOCAL_MACHINE
        elif hkey == "HKEY_USERS":
            return winreg.HKEY_USERS
        elif hkey == "HKEY_CURRENT_CONFIG":
            return winreg.HKEY_CURRENT_CONFIG
        else:
            raise ValueError("Invalid root key: " + hkey)


    def get_registry_value(self):
        """Get a value from the Windows registry by passing the root key,
        subkey, and value name.

        Returns:
            str: the value from the registry
        """
        # Open the registry key
        try:
            hkey_const = self.get_hkey_const(self._hkey)
            # Open the registry key
            registry_key = winreg.OpenKey(hkey_const, self._sub_key)
            # Get the value
            value, value_type = winreg.QueryValueEx(registry_key, self._value_name)
            # Close the registry key
            winreg.CloseKey(registry_key)
            return value
        except FileNotFoundError:
            return "Not found"



MIKERO_TOOLS_PATH = GetRegistryValues("HKEY_LOCAL_MACHINE", r"HKEY_CURRENT_USER\Software\Mikero\ArmA3p", "path")

print(MIKERO_TOOLS_PATH)

#get mikero tools path
    #key = HKEY_CURRENT_USER\Software\Mikero\ArmA3p
        #ValueName = path
        #  returns mikero tools path ie C:\Program Files (x86)\Mikero\DePboTools

#get arma3p (pdrive builder) path
    #key = HKEY_CURRENT_USER\Software\Mikero\ArmA3p
        #valuename = exe
        #returns path and.cmd name ie C:\Program Files (x86)\Mikero\DePboTools\bin\ArmA3p.cmd

#get arma3 Addon Builder Path
    #key = =HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\bohemia interactive\AddonBuilder
        #valuename = path
        #returns path ie D:\Games\Steam\steamapps\common\Arma 3 Tools\AddonBuilder


#get Arma3 path
    #key = HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\bohemia interactive\ArmA3
        #valuename = main
            #returns path ie C:\SteamLibrary\steamapps\common\Arma 3
