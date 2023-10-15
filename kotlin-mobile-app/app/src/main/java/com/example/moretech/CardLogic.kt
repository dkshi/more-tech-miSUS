package com.example.moretech

import android.app.Dialog
import android.widget.Button
import androidx.appcompat.widget.SwitchCompat
import com.example.moretech.models.FilterOfficeResponse

class CardLogic {
    lateinit var rampSwitch: SwitchCompat
    lateinit var kepSwitch: SwitchCompat
    lateinit var departmentSwitch: SwitchCompat
    lateinit var rkoSwitch: SwitchCompat
    lateinit var suoSwitch: SwitchCompat
    lateinit var submitButton: Button

    interface CardInteractionListener {
        fun onOptionsSelected(options: FilterOfficeResponse)
    }

    // Declare a variable to hold the listener reference
    private var listener: CardInteractionListener? = null

    // ...

    fun setCardInteractionListener(listener: CardInteractionListener) {
        this.listener = listener
    }

    fun initializeViews(dialog: Dialog) {
        rampSwitch = dialog.findViewById(R.id.rampSwitch)
        kepSwitch = dialog.findViewById(R.id.kepSwitch)
        departmentSwitch = dialog.findViewById(R.id.departmentSwitch)
        rkoSwitch = dialog.findViewById(R.id.rkoSwitch)
        suoSwitch = dialog.findViewById(R.id.suoSwitch)
        submitButton = dialog.findViewById(R.id.submitButton)


        // Set up listeners for switches and button
        kepSwitch.setOnCheckedChangeListener { _, isChecked ->
            // Handle switch1 state change
            if (isChecked) {
                // Switch1 is checked
            } else {
                // Switch1 is unchecked
            }
        }

        rampSwitch.setOnCheckedChangeListener { _, isChecked ->
            // Handle switch2 state change
            if (isChecked) {
                // Switch2 is checked
            } else {
                // Switch2 is unchecked
            }
        }

        departmentSwitch.setOnCheckedChangeListener { _, isChecked ->
            // Handle switch1 state change
            if (isChecked) {
                // Switch1 is checked
            } else {
                // Switch1 is unchecked
            }
        }

        rkoSwitch.setOnCheckedChangeListener { _, isChecked ->
            // Handle switch1 state change
            if (isChecked) {
                // Switch1 is checked
            } else {
                // Switch1 is unchecked
            }
        }

        suoSwitch.setOnCheckedChangeListener { _, isChecked ->
            // Handle switch1 state change
            if (isChecked) {
                // Switch1 is checked
            } else {
                // Switch1 is unchecked
            }
        }

        submitButton.setOnClickListener {

            var options1 = FilterOfficeResponse(null, null, null, null, null)
            val list1 = listOf<String>("kep", "ramp", "my_branch", "rko", "suo")
            val list2 = listOf(kepSwitch, rampSwitch, departmentSwitch, rkoSwitch, suoSwitch)

            for (i in list1.indices) {
                if (list2[i].isChecked) {
                    when(list1[i]){
                        "kep" -> options1.kep = list2[i].isChecked
                        "ramp" -> options1.ramp = list2[i].isChecked
                        "my_branch" -> options1.my_branch = list2[i].isChecked
                        "rko" -> options1.rko = list2[i].isChecked
                        "suo" -> options1.suo = list2[i].isChecked
                    }
                }
            }
            listener?.onOptionsSelected(options1)


//            val options = mapOf<String, Boolean>("ramp" to rampSwitch.isChecked, "kep" to kepSwitch.isChecked,
//                "my_branch" to departmentSwitch.isChecked, "rko" to rkoSwitch.isChecked, "suo" to suoSwitch.isChecked)
//


        }
    }
}