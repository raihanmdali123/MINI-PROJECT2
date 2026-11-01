# MODULE 2
# SMART CANTEEN BILLING AND ORDER ANALYZER

# Display menu and price
print("========== MENU AND PRICE ==========")
print("1. Veg Sandwich : 60 Rs")
print("2. Masala Dosa : 80 Rs")
print("3. Chole Rice : 90 Rs")
print("4. Paneer Roll : 100 Rs")
print("5. Tea : 20 Rs")
sub_total=0

while True:
    item = int(input("CHOOSE ITEM NUMBER(1-5): "))
    
    if item >5 or item <=0 :
           print("INVALID CHOICE: ")
           
           break
    quant = int(input("ENTER QUANTITY(1-10): "))
    if quant<=0 or quant>10 :
           print("QUANTITY MUST BE IN BETWEEN (0-10)")
           
           break
    elif item == 1:
        print("ADDED: Veg Sandwich ","X ",quant,"=","₹",float(60*quant))
        sub_total +=float(60*quant)
    elif item == 2:
            print("ADDED: Masala Dosa ","X ",quant,"=","₹",float(80*quant))
            sub_total +=float(80*quant)
    elif item == 3:
            print("ADDED: Chole Rice ","X ",quant,"=","₹",float(90*quant))
            sub_total +=float(90*quant)
    elif item == 4:
            print("ADDED: Panner Roll ","X ",quant,"=","₹",float(100*quant))
            sub_total +=float(100*quant)
    elif item == 5:
            print("ADDED: Tea","X ",quant,"= ₹",float(20*quant))
            sub_total +=float(20*quant)


    Adding_Another_item= input("Add another item? (Yes/NO) : ").upper()
    if Adding_Another_item=="NO":
        break

print("---===== RECEIPT =====---")

if sub_total > 500:
        discount = (sub_total * 10) / 100
elif sub_total > 250:
     discount = (sub_total * 5) / 100
else:
     discount = 0
print(f"Subtotal: ₹ {sub_total}\nDiscount: ₹ {discount}\nTotal: ₹ {sub_total - discount}")
print("THANK YOU SIR")
