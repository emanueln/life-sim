# Death module

def handle_deaths(sims, dead_sims):
    live_sims = list(filter(lambda sim: sim.alive, sims))
    dead_sims += list(filter(lambda sim: not sim.alive, sims))
    return_sims = []
    for sim in live_sims:
        if sim.partner_id > 0 and not next(filter(lambda x: x.id == sim.partner_id, sims), None).alive:
            #print("%s's partner died. They are grieving." % sim.name)
            sim.grieving = True
            sim.partner_id = 0
        elif sim.grieving:
            #print("%s is no longer grieving. They will start looking for a partner." % sim.name)
            sim.grieving = False
        elif sim.age < 9 and sim.alive:
            parent =  next(filter(lambda x: x.id == sim.genes.mother_id, sims), None)
            if not parent.alive:
                sim.kill(2)
        return_sims.append(sim)
    return return_sims, dead_sims