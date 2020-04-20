import sys
from model.modelclasses import ArchitectureModel
from utils.utils import Utils

##############################################################################################################
  
if __name__ == '__main__':

    parser = Utils.init_parse_argument()
    args = parser.parse_args()
    outputfolder = '.' 
    if args.outputfolder != None:
        outputfolder = args.outputfolder
    print('python version='+sys.version)
    print('****************** params ******************')
    print('outputfolder='+outputfolder)
    print('********************************************')

    acmodel = ArchitectureModel('empty modele','empty modele.CASTArchitect', ArchitectureModel.TYPE_FORBIDDEN,'JEE', outputfolder)
    acmodel.generate_model()
    


