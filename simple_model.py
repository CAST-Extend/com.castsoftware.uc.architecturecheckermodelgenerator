from model.modelclasses import ArchitectureModel, MemberOf, Property,Layer, Criteria, ExcludedFrom, Link

##############################################################################################################
  
  
def create_app_specific_sets_and_layers(acmodel):
        # Acceptance
        saccept = 'set Acceptance'
        p=Property(Property.NAME_PATH,Property.OP_LIKE,['%-acceptance\\%' , '%_acceptance\\%',])
        c=Criteria(Criteria.TYPE_SELECTION_CRITERIA, True, False)
        c.add_property(p)
        s=Layer(saccept, Layer.TYPE_SET)
        s.add_criteria(c)
        acmodel.add_layer(s)
        
        p=Property(Property.NAME_PATH,Property.OP_LIKE,['%\\Kernel\\%'])
        c=Criteria(Criteria.TYPE_SELECTION_CRITERIA, True, False)
        c.add_property(p)
        c.add_excludedfromset(ExcludedFrom(saccept))
        c.add_excludedfromset(ExcludedFrom(Layer.set_Java_Instantiated))
        c.add_excludedfromset(ExcludedFrom(Layer.set_Java_Properties_File))
        s=Layer('set Kernel', Layer.TYPE_SET, True)
        s.add_criteria(c)
        acmodel.add_layer(s)  
  
        listlayerstocreate = ['layer1','layer2','layer3']
  
        for l in listlayerstocreate:
            p=Property(Property.NAME_PATH,Property.OP_LIKE,['%\\' + l + '\\%'])
            c=Criteria(Criteria.TYPE_SELECTION_CRITERIA, True, False)
            c.add_property(p)
            c.add_memberofset(MemberOf('set Kernel'))
            c.add_excludedfromset(ExcludedFrom(saccept))
            c.add_excludedfromset(ExcludedFrom(Layer.set_Java_Instantiated))
            c.add_excludedfromset(ExcludedFrom(Layer.set_Java_Properties_File))
            s=Layer(l, Layer.TYPE_LAYER, True)
            s.add_criteria(c)
            acmodel.add_layer(s)   
  
def create_app_specific_links(acmodel):
    acmodel.add_link(Link('layer1','layer2'))
  
if __name__ == '__main__':

    acmodel = ArchitectureModel('simple model','simple model.CASTArchitect', ArchitectureModel.TYPE_FORBIDDEN, 'JEE,Cobol')
    create_app_specific_sets_and_layers(acmodel)
    create_app_specific_links(acmodel)
    acmodel.generate_model()

    
