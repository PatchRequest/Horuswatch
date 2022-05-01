<template>
    <div >
        <div>
            <ul class="steps">
                <li class="step step-primary">Receive Hashes</li>
                <li class="step step-primary">Test Hashes</li>
                <li class="step">Analyze Findings</li>
                <li class="step">Display Results</li>
            </ul>
        </div>
        
        
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Total Possible Hashes</div>
                <div class="stat-value">89,400</div>
            </div>
        
        </div>
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Hashes Tested</div>
                <div class="stat-value">12,400</div>
            </div>
        
        </div>
        <div class="stats shadow">
  
            <div class="stat">
                <div class="stat-title">Percentage</div>
                <div class="stat-value">37%</div>
            </div>
        
        </div>
        <div>
            <progress class="progress progress-secondary w-56" value="170" max="300"></progress>
        </div>
      
    </div>



 
</template>

<script>
export default {
    name: 'StatusPage'
}
</script>