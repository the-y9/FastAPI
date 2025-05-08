#%%
StandardLife= 400000
LifeAlert= 260000
RemainingLife= 7000
ConsumedLife =StandardLife-RemainingLife

print("Life alert %",LifeAlert/StandardLife*100)
print("consumed life%",ConsumedLife/StandardLife*100)
print("remaining life%",RemainingLife/StandardLife*100)

# %%
#%%
y = LifeAlert - (LifeAlert * 0.5)
lr = LifeAlert - (LifeAlert * 0.75)
print("Yellow Alert%", y/StandardLife*100)
print(lr)
print("Light Red Alert%", lr/StandardLife*100)
#%%
if RemainingLife <= LifeAlert:
    if RemainingLife > y:
        flag = "CardLightWarning col-md-12"
    elif RemainingLife <= y and RemainingLife > lr:
        flag = "CardLightDanger col-md-12"
    else:
        flag = "CardDanger col-md-12"
print(flag)
# %%
