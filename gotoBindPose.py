
import sys
import os
script_dir = os.path.dirname(__file__)


sys.path.append(r'{}'.format(script_dir))
try:
    del sys.modules['Skeleton2CAT']    
except:
	pass

from Skeleton2CAT import Skeleton2CAT
sk2cat = Skeleton2CAT()
sk2cat.selectReturnToBindPose()